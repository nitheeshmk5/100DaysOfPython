from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome to home page"


@app.route('/<name>')
def home(name):
    res = requests.get(f'https://api.genderize.io?name={name}')
    gender = res.json()
    gender_name = gender['gender']
    agify = requests.get(f'https://api.agify.io?name={name}')
    age_res = agify.json()
    guess_age = age_res['age']
    return render_template('index.html' , name=name,gender = gender_name,age = guess_age)

if __name__ == '__main__':
    app.run(debug=True)