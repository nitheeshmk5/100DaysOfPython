from flask import Flask, render_template
import requests


res = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
all_blogs = res.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",all_blogs=all_blogs)


@app.route('/post/<int:id>')
def blog(id):
    req_post = None
    for blog_post in all_blogs:
        if blog_post['id'] == id:
            req_post = blog_post
    return render_template('post.html',blog=req_post)


if __name__ == "__main__":
    app.run(debug=True)
