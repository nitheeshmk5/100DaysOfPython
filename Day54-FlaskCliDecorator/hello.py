from flask import Flask
import time
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

def delay_functions(function):
    def wrap_function():
        time.sleep(3)
        function()
    return wrap_function

@delay_functions
def say_hello():
    print("Hello")

say_hello()