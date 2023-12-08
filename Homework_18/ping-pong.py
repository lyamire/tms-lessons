from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    return f'''
        <a href="/pong">pong</a>
    '''

@app.route('/pong')
def pong():
    return f'''
        <a href="/ping">ping</a>
    '''


if __name__ == '__main__':
    app.run()
