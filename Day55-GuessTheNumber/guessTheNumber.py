from flask import Flask
from random import randint

app = Flask(__name__)
number = randint(1,10)

@app.route('/')
def display_home():
    return '<h1>Guess the number (1 - 10) </h1>' \
            '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'


@app.route('/<int:inp>')
def display_output(inp):
    if inp == number:
        return "<h1 style='color:red'>You are correct,you found it</h1>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"
    elif inp < number:
        return "<h1 style='color:blue'>You are too lower! </h1>" \
                "<img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
    elif inp > number:
        return "<h1 style='color:violet'>You are too high! </h1>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"
    else:
        return "Enter a valid input"


#print(number)
if __name__ == "__main__":
    app.run(debug=True)