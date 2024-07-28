import json

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
with open('config.json', 'r') as c:
    params=json.load(c)["params"];
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:SQL%402004@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contact(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


@app.route("/")
def home():
    return render_template("index.html",params=params)


@app.route("/about")
def about():
    return render_template("about.html",params=params)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, phone_num=phone, msg=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        return  '<h1>Success</h1>'
    return render_template('contact.html',params=params)


app.run(debug=True)
