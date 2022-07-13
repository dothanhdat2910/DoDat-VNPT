from crypt import methods
from re import T
from flask import Flask, render_template,request
from flask_mail import Mail, Message
import os
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dothanhdatk18@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/home',methods = ['GET','POST'])
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        msg = Message('Hey',sender='')
