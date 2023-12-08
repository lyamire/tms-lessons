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
        connection.execute('UPDATE article '
                               ' SET title = ?, text = ?, author = ?, like_count = ?'
                               ' WHERE id = ?', data)


@app.route('/')
@app.route('/articles')
def articles_view():
    articles = get_all_articles()
    articles_html = '\n'.join(f'<li><a href="/article/{article.id}">{article.title}</a></li>' for article in articles)

    return f'''
        <html>
            <head>
                <title>Articles APP</title>
            </head>
            <body>
                <h1>All Articles</h1>
                <ul>
                    {articles_html}
                </ul>
            </body>
        </html>
        '''

@app.route('/article/<int:id>')
def article_view(id: int):
    try:
        article = get_article(id)
    except ValueError as e:
        abort(404, e)
    return f'''
        <html>
            <head>
                <title>Articles APP</title>
            </head>
            <body>
                <a href="/articles">Go to home page</a>
                <h1>{article.title}</h1>
                <h3>{article.author}</h3>
                <p>{article.text}</p>
                <p>like count: {article.like_count}</p>
                <form method="post" action="/article/like" >
                    <input type="hidden" value="{article.id}" name="article_id"/>
                    <input type="submit" value="Like">
                </form>
            </body>
        </html>
        '''

@app.route('/article/like', methods=['POST'])
def like_article():
    article_id = int(request.form['article_id'])
    article = get_article(article_id)
    liked_articles = session.setdefault('liked_articles', set())
    if article.id in liked_articles:
        article.like_count -= 1
        liked_articles.remove(article.id)
    else:
        article.like_count += 1
        liked_articles.add(article.id)
    save_article(article)
    return redirect(f'/article/{article.id}')


if __name__ == '__main__':
    app.run(port=8080, debug=True)

