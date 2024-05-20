from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrap():
        func()
    return wrap


@app.route('/')
def hi():
    return f'Hello'


if __name__ == '__main__':
    app.run(debug=True)