from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    name = request.args.get('name')
    return f'<p>Hello, <i>{name}</i>!</p>'


if __name__ == '__main__':
    app.run()
