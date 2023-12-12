from dataclasses import dataclass, field
import sqlite3

from flask import Flask, redirect, request, abort, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@dataclass
class Product:
    id: int
    name: str
    description: str
    category: str

@dataclass
class Category:
    id: int
    name: str
    products: list[Product] = field(default_factory=list)

@dataclass
class User:
    id: int
    login: str
    password: str

@dataclass
class FavoriteProduct:
    user_id: int
    product_id: int

class Shop:
    __filename: str

    def __init__(self, filename: str):
        self.__filename = filename
        db = sqlite3.connect(filename)

        db.execute('''
        create table IF NOT EXISTS categories (
            id   integer constraint categories_pk primary key autoincrement,
            name varchar(64) not null
        );''')

        db.execute(
            '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER constraint products_pk PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            description  VARCHAR NOT NULL,
            category_id INTEGER constraint products_categories_fk references categories
        );''')

        db.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER NOT NULL
                constraint user_pk
                    primary key autoincrement,
            login TEXT NOT NULL,
            password TEXT NOT NULL
        );''')

        db.execute('''
            CREATE TABLE IF NOT EXISTS favorite_products (
            user_id INTEGER NOT NULL 
                constraint favorite_products_user_id_fk
                    references user,
            product_id INTEGER NOT NULL 
                constraint favorite_products_products_id_fk
                    references products
        );''')

    def get_products(self) -> list[Product]:
        response = sqlite3.connect(self.__filename).execute('SELECT products.id, products.name, description, categories.name '
                                                            'FROM products JOIN categories ON products.category_id = categories.id').fetchall()
        return [Product(*values) for values in response]

    def get_product(self, product_id: int) -> Product:
        response = sqlite3.connect(self.__filename).execute(
            'SELECT products.id, products.name, description, categories.name '
            'FROM products JOIN categories ON products.category_id = categories.id WHERE products.id = ? ',
            (product_id,))
        row = response.fetchall()
        if len(row) != 1:
            raise ValueError(f'Expected 1 object with id {product_id}, got {len(row)}')
        return Product(*row[0])

    def load_categories(self) -> list[Category]:
        products = sqlite3.connect(self.__filename).execute(
            'SELECT products.id, products.name, products.description, '
            'categories.id as category_id, categories.name as category_name '
            'FROM products '
            'JOIN categories ON categories.id = products.category_id').fetchall()

        categories = {}
        for product in products:
            category = categories.get(product[3])
            if category is None:
                category = Category(product[3], product[4])
                categories[category.id] = category

            product = Product(product[0], product[1], product[2], product[4])
            category.products.append(product)

        return list(categories.values())

    def load_products_by_category(self, category_id: int) -> list[Product]:
        response = sqlite3.connect(self.__filename).execute(
            f'SELECT id, name, description, category_id FROM products WHERE category_id = ?',
            (category_id,))
        rows = response.fetchall()
        return [Product(*row) for row in rows]

    def get_category(self, category_id: int) -> Category:
        response = sqlite3.connect(self.__filename).execute('SELECT id, name FROM categories WHERE id = ?',
                                                            (category_id, ))
        row = response.fetchall()
        assert len(row) == 1  #
        return Category(*row[0])

    def get_user(self, login: str) -> User | None:
        with sqlite3.connect(self.__filename) as connection:
            response = connection.execute('SELECT id, login, password FROM user WHERE login = ?', (login, ))
            row = response.fetchall()
            if len(row) > 1:
                raise ValueError(f'Expected 1 object with name = {login}, got {len(row)}')
            elif len(row) == 0:
                return None
            return User(*row[0])

    def create_user(self, login: str, password: str) -> int:
        with sqlite3.connect(self.__filename) as connection:
            acc = self.get_user(login)
            if acc is None:
                cursor = connection.execute('INSERT INTO user (login, password) VALUES (?,?)', [login, password])
                return cursor.lastrowid
            raise Exception

    def is_favorite_product_for_user(self, user_id: int, product_id: int) -> bool:
        with sqlite3.connect(self.__filename) as connection:
            response = connection.execute('SELECT user_id, product_id FROM favorite_products WHERE user_id = ? and product_id = ?', [user_id, product_id])
            row = response.fetchall()
            return len(row) > 0

    def set_favorite_product_for_user(self, user_id: int, product_id: int):
        with sqlite3.connect(self.__filename) as connection:
            if self.is_favorite_product_for_user(user_id, product_id):
                response = connection.execute('DELETE FROM favorite_products WHERE user_id = ? and product_id = ?', [user_id, product_id])
            else:
                response = connection.execute('INSERT INTO favorite_products (user_id, product_id) VALUES (?,?)', [user_id, product_id])

    def load_favorite_products(self, user_id: int) -> list[Product]:
        with sqlite3.connect(self.__filename) as connection:
            response = connection.execute('SELECT products.id, products.name, description, categories.name '
                                          'FROM products JOIN categories ON products.category_id = categories.id '
                                          'WHERE products.id in (SELECT product_id FROM favorite_products WHERE user_id = ?)',[user_id])
            return [Product(*values) for values in response]


my_shop = Shop('shop.sqlite')

def check_auth(func):
    def wrapper(*args, **kwargs):
        if not session.get('is_authenticated'):
            return redirect(f'/auth')
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper

def render_page(title: str, content: str) -> str:
    has_auth = bool(session.get('is_authenticated'))
    return f'''
        <html>
            <head>
                <title>{title}</title>
            </head>
            <body>
            <div class="menu" style="text-align: right;">
                {'<span><a href="/logout">Logout</a></span>' if has_auth else ''}
            </div>
            <h1><a href="/">Go to main page</a></h1>
            <h1><a href="/products/favorites">Go to favorite products page</a></h1>
            <span><h1>{title}</h1></span>
                <ul>
                    {content}
                </ul>
            </body>
        </html>
        '''

@app.route('/products')
@check_auth
def all_products_view():
    products = my_shop.get_products()
    products_html = generate_products_list_html(products)
    return render_page('Products', products_html)

@app.route('/products/favorites')
@check_auth
def favorites_view():
    user_id = int(session.get('user_id'))
    favorite_products = my_shop.load_favorite_products(user_id)
    products_html = generate_products_list_html(favorite_products)
    return render_page('Favorites', products_html)

def generate_products_list_html(products):
    products_html = '\n'.join(f'<li><a href="/product/{product.id}">{product.name}</a></li>' for product in products)
    return f'<ul>{products_html}</ul>'


@app.route('/product/<int:id>')
@check_auth
def product_view(id: int):
    try:
        product = my_shop.get_product(id)
        user_id = session['user_id']
        is_favorite = my_shop.is_favorite_product_for_user(user_id, id)
    except ValueError as e:
        abort(404, e)

    content = f'''<h1>{product.name}</h1>
                  <p>{product.description}</p>
                  <p>{product.category}</p>
                  <form method="post" action="/api/product/{product.id}/favorite">
                     <input type="submit" value="{'Favorite &#10027' if is_favorite else 'Add to Favorite'}">
                  </form>'''
    return render_page('Product', content)

@app.route('/api/product/<int:product_id>/favorite', methods=['POST'])
@check_auth
def favorite_product(product_id):
    user_id = int(session.get('user_id'))
    my_shop.set_favorite_product_for_user(user_id, product_id)
    return redirect(f'/product/{product_id}')

def generate_category_html(category):
    return f'''
      <a href="/category/{category.id}">{category.name}</a>
    <li>
      {generate_products_list_html(category.products)}
    </li>'''

@app.route('/')
@check_auth
def main_page():
    categories = my_shop.load_categories()
    categories_html = '\n'.join(generate_category_html(category) for category in categories)

    main_page_template = f'''<ul>
                                {categories_html}
                             </ul>'''
    return render_page('Main page', main_page_template)

@app.route('/category/<int:category_id>')
@check_auth
def category_view(category_id: int):
    category = my_shop.get_category(category_id)
    category.products = my_shop.load_products_by_category(category_id)
    products_html = generate_products_list_html(category.products)
    return render_page(category.name, products_html)

@app.route('/register')
def register_view():
    return f'''
    <form action="/api/register" method="POST">
        Login <input type="text" name="login"></br>
        Password <input type="password" name="password"></br>
        <input type="submit" value="Sign up"/>
    </form>
    <a href="/auth">Authorization</a>
    '''

@app.route('/api/register', methods=['POST'])
def register():
    username = request.form['login']
    password = request.form['password']
    account_id = my_shop.create_user(username, password)
    session['is_authenticated'] = True
    session['user_id'] = account_id
    return redirect('/')

@app.route('/auth')
def auth_view():
    return f'''
    <form action="/api/auth" method="POST">
        Login <input type="text" name="login"></br>
        Password <input type="password" name="password"></br>
        <input type="submit" value="Sign in">
    </form>
    <a href="register">Register</a>
    '''

@app.route('/api/auth', methods=['POST'])
def authenticate():
    try:
        login = request.form['login']
        password = request.form['password']
        acc = my_shop.get_user(login)
        if acc and acc.password == password:
            session['is_authenticated'] = True
            session['user_id'] = acc.id
            return redirect('/')
        else:
            raise Exception('Ошибка авторизации')
    except Exception:
        return redirect('/error_auth')

@app.route('/error_auth')
def error_auth_view():
    return f'Ошибка авторизации. <a href="/auth">Попробуйте снова</a>'

@app.route('/logout')
def logout():
    session['is_authenticated'] = None
    session['user_id'] = None
    return redirect('/')


if __name__ == "__main__":
    app.run(port=8080, debug=True)
