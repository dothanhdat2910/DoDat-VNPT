from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dothanhdatk18@gmail.com'
app.config['MAIL_PASSWORD'] = 'vkrosjgcepfboezc'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)



@app.route('/home', methods= ['GET', 'POST'])
@app.route('/', methods= ['GET', 'POST'])
def home():
    if request.method == 'POST':
        NameTitle = request.form["Title"]
        Email = request.form["Email"]
        msg = Message(NameTitle, sender='dothanhdatk18@gmail.com', recipients=[Email])
        msg.body = request.form["Body"]
        mail.send(msg)
        return "Sent email"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)