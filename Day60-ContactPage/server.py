from flask import Flask,render_template,request
import requests
import smtplib,os
from dotenv import load_dotenv
from waitress import serve

all_blogs = requests.get('https://api.npoint.io/674f5423f73deab1e9a7').json()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home_page():
    return render_template('index.html',all_blogs=all_blogs)


@app.route("/about")
def about_page():
    return render_template('about.html')

load_dotenv()

my_email = os.getenv('MAIL')
password = os.getenv('PASS')

@app.route('/contact',methods=['GET','POST'])
def contact_page():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        msg = data["message"]

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login( user = my_email,password = password)

            connection.sendmail(
                from_addr = my_email,
                to_addrs = my_email,
                msg=f"Subject:Contact form submitted by {name}\n\nemail : {email}\nphone : {phone}\nmessage : \n{msg}"
                )
        return render_template('contact.html',msg_sent = True)
    else:
        return render_template('contact.html',msg_sent = False)




@app.route('/post/<int:id>')
def post_page(id):
    return render_template('post.html', all_blogs=all_blogs[id - 1],post_id = id )


if __name__ == "__main__":
    serve(app,host='0.0.0.0',port=8000)