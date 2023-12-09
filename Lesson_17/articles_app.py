from dataclasses import dataclass
from flask import Flask, redirect, request, abort, session
from flask_session import Session
import sqlite3

DATABASE_FILE = 'articles_db.sqlite'

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str
    like_count: int

@dataclass
class Account:
    id: int
    name: str
    password: str

@dataclass
class Favorites:
    article_id: int
    user_id: int

def get_all_articles() -> list[Article]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, title, text, author, like_count FROM article')
        return [Article(*values) for values in execution_result.fetchall()]

def get_article(article_id: int) -> Article:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, title, text, author, like_count FROM article WHERE id = ?',
                                              (article_id,))
        row = execution_result.fetchall()
        if len(row) != 1:
            raise ValueError(f'Expected 1 object with id {article_id}, got {len(row)}')
        return Article(*row[0])

def save_article(article: Article):
    with sqlite3.connect(DATABASE_FILE) as connection:
        data = (article.title, article.text, article.author, article.like_count, article.id)
        connection.execute('UPDATE article SET title = ?, text = ?, author = ?, like_count = ? WHERE id = ?', data)

def get_user(login: str) -> Account | None:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, name, password FROM user WHERE name = ?',
                                              (login,))
        row = execution_result.fetchall()
        if len(row) > 1:
            raise ValueError(f'Expected 1 object with name {login}, got {len(row)}')
        elif len(row) == 0:
            return None
        return Account(*row[0])

def create_user(username: str, password: str) -> int:
    with sqlite3.connect(DATABASE_FILE) as connection:
        acc = get_user(username)
        if acc is None:
            cursor = connection.execute('INSERT INTO user (name, password) VALUES (?,?)', [username, password])
            return cursor.lastrowid  # последний добавленный account_id
        raise Exception

def like_article_for_user(article_id: int, user_id: int):
    article = get_article(article_id)

    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT article_id, user_id FROM favorite_articles WHERE article_id = ? and user_id = ?',
            [article_id, user_id])
        row = execution_result.fetchall()
        if len(row) > 0:
            article.like_count -= 1
            execution_result = connection.execute(
                'delete from favorite_articles WHERE article_id = ? and user_id = ?',
                [article_id, user_id])
        else:
            article.like_count += 1
            execution_result = connection.execute(
                'insert into favorite_articles (article_id, user_id) values (?, ?)',
                [article_id, user_id])

    save_article(article)


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
            <span><h1>{title}</h1></span>
                <ul>
                    {content}
                </ul>
            </body>
        </html>
        '''

@app.route('/')
@app.route('/articles')
@check_auth
def articles_view():
    articles = get_all_articles()
    articles_html = '\n'.join(f'<li><a href="/article/{article.id}">{article.title}</a></li>' for article in articles)

    return render_page('Articles', articles_html)

@app.route('/article/<int:id>')
@check_auth
def article_view(id: int):
    try:
        article = get_article(id)
    except ValueError as e:
        abort(404, e)
    content = f'''<h3>{article.author}</h3>
                <p>{article.text}</p>
                <p>like count: {article.like_count}</p>
                <form method="post" action="/api/article/like">
                    <input type="hidden" value="{article.id}" name="article_id">
                    <input type="submit" value="Like">
                </form>
                <a href="/articles">Go to home page</a>'''
    return render_page(article.title, content)

@app.route('/api/article/like', methods=['POST'])
@check_auth
def like_article():
    article_id = int(request.form['article_id'])
    user_id = int(session.get('user_id'))

    like_article_for_user(article_id, user_id)

    return redirect(f'/article/{article_id}')

@app.route('/auth')
def auth_view():
    content = f'''
    <form action="/api/auth" method="post">
        Login <input type="text" name="login"></br>
        Password <input type="password" name="password"></br>
        <input type="submit" value="Sign in">
    </form>
    <a href="register">Registration</a>
    '''
    return render_page('Authorization', content)

@app.route('/api/auth', methods=['POST'])
def authenticate():
    try:
        username = request.form['login']
        password = request.form['password']
        acc = get_user(username)
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
    return render_page('Authorization error', f'Ошибка авторизации. <a href="/auth">Попробуйте снова</a>')

@app.route('/register')
def register_view():
    content = f'''
    <form action="/api/register" method="post">
        Login <input type="text" name="login"></br>
        Password <input type="password" name="password"></br>
        <input type="submit" value="Sign up">
    </form>
    <a href="/auth">Authorization</a>
    '''
    return render_page('Registration', content)

@app.route('/api/register', methods=['POST'])
def register():
    username = request.form['login']
    password = request.form['password']
    account_id = create_user(username, password)
    session['is_authenticated'] = True
    session['user_id'] = account_id
    return redirect('/')

@app.route('/logout')
def logout():
    session['is_authenticated'] = None
    session['user_id'] = None
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8080, debug=True)

