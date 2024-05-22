from flask import Flask,render_template
import requests


all_blogs = requests.get('https://api.npoint.io/674f5423f73deab1e9a7').json()


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home_page():
    return render_template('index.html',all_blogs=all_blogs)


@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post_page(id):
    return render_template('post.html', all_blogs=all_blogs[id - 1],post_id = id )


if __name__ == "__main__":
    app.run(debug=True)