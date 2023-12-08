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

    def load_products(self) -> list[Product]:
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

    def load_products_by_category(self,category_id: int):
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


my_shop = Shop('shop.sqlite')

@app.route('/products')
def all_products_view():
    products = my_shop.load_products()
    products_html = generate_products_list_html(products)
    return f'''
    <html>
    <head>
        <title>Shop</title>
    </head>
    <body>
        <h1><a href="/">Go to main page</a></h1>
        <h1><a href="/products/favorites">Go to favorite products page</a></h1>
        <h1>Products</h1>
        {products_html}
    </body>
    </html>
    '''

@app.route('/products/favorites')
def favorites_view():
    products = my_shop.load_products()
    favorites_products = session.setdefault('favorites_products', set())
    favorite_products = filter(lambda x: x.id in favorites_products, products)
    products_html = generate_products_list_html(favorite_products)
    return f'''
        <html>
        <head>
            <title>Shop</title>
        </head>
        <body>
            <h1><a href="/">Go to main page</a></h1>
            <h1><a href="/products">Go to all products page</a></h1>
            <h1>Favorite products</h1>
            {products_html}
        </body>
        </html>
        '''

def generate_products_list_html(products):
    products_html = '\n'.join(f'<li><a href="/product/{product.id}">{product.name}</a></li>' for product in products)
    return f'<ul>{products_html}</ul>'


@app.route('/product/<int:id>')
def product_view(id: int):
    try:
        product = my_shop.get_product(id)
    except ValueError as e:
        abort(404, e)
    favorites_products = session.setdefault('favorites_products', set())
    is_favorite = id in favorites_products
    return f'''
            <html>
                <head>
                    <title>Product</title>
                </head>
                <body>
                    <a href="/products">Go to home page</a>
                    <h1>{product.name}</h1>
                    <p>{product.description}</p>
                    <p>{product.category}</p>
                    <form method="post" action="/product/{product.id}/favorite">
                        <input type="submit" value="{'Favorite &#10027' if is_favorite else 'Add to Favorite'}">
                    </form>
                </body>
            </html>
            '''

@app.route('/product/<int:product_id>/favorite', methods=['POST'])
def favorite_product(product_id):
    favorites_products = session.setdefault('favorites_products', set())
    if product_id in favorites_products:
        favorites_products.remove(product_id)
    else:
        favorites_products.add(product_id)
    session['favorites_products'] = favorites_products
    return redirect(f'/product/{product_id}')

def generate_category_html(category):
    return f'''
      <a href="/category/{category.id}">{category.name}</a>
    <li>
      {generate_products_list_html(category.products)}
    </li>'''

@app.route('/')
def main_page():
    categories = my_shop.load_categories()
    categories_html = '\n'.join(generate_category_html(category) for category in categories)

    main_page_template = f'''
    <html>
    <head>
        <title>Shop</title>
    </head>
    <body>
        <h1><a href="/products">Go to all products page</a></h1>
        <h1><a href="/products/favorites">Go to favorite products page</a></h1>
        <h1>Main Page</h1>
        <ul>
            {categories_html}
        </ul>
    </body>
    </html>
    '''
    return main_page_template

@app.route('/category/<int:category_id>')
def category_view(category_id: int):
    category = my_shop.get_category(category_id)
    category.products =my_shop.load_products_by_category(category_id)
    products_html = generate_products_list_html(category.products)
    return f'''
        <html>
        <head>
            <title>Shop</title>
        </head>
        <body>
            <h1><a href="/">Go to main page</a></h1>
            <h1><a href="/products">Go to all products page</a></h1>
            <h1><a href="/favorite-products">Go to favorite products page</a></h1>
            <h1>{category.name}</h1>
            {products_html}
        </body>
        </html>
        '''



if __name__ == "__main__":
    app.run(port=8080, debug=True)
