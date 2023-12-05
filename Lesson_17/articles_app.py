from dataclasses import dataclass
from flask import Flask, request
import sqlite3

DATABASE_FILE = 'articles_db.sqlite'

app = Flask(__name__)

@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str

def get_all_articles() -> list[Article]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, title, text, author FROM article')
        return [Article(*values) for values in execution_result.fetchall()]

def get_article(article_id) -> Article:
    with sqlite3.connect(DATABASE_FILE) as connection:
        excution_result = connection.execute('SELECT id, title, text, author FROM article WHERE id = ?', (article_id))
        row = excution_result.fetchall()
        if len(row) != 1:
            raise ValueError(f'Expected 1 object with id {article_id}, got {len(row)}')
        return Article(*row[0])

def save_article(article: Article):
    with sqlite3.connect(DATABASE_FILE) as connection:
        data = (article.title, article.text, article.author, article.id)
        connection.execute('UPDATE article '
                               ' SET title = ?, text = ?, author = ?'
                               ' WHERE id = ?', data)


@app.route('/')
@app.route('/articles')
def articles_view():
    articles = get_all_articles()
    articles_html = '\n'.join(f'<li>{article.title}</li>' for article in articles)

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


if __name__ == '__main__':
    app.run(port=8080, debug=True)

