'''from flask_mail import *
from flask import *
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='lcablelca@gmail.com'
app.config['MAIL_PASSWORD']='lifechoices'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
@app.route('/')
def Index():

    msg=Message('Hello', sender='{{',recipients=['elantrahufkie@gmail.com'])
    msg.body='HI this ia an attempt at sending flask email'
    mail.send(msg)
    return render_template('email_form.html')
if __name__=='__main__':
    app.run(debug=True)
'''



from flask_mail import *
from flask import *
import smtplib

app=Flask(__name__)
@app.route('/')
def Index():
    return  render_template('email_form.html')

@app.route('/contact/')
def contact():
    return render_template('email_form.html')

@app.route('/send_email/',  methods=['POST', 'GET'])
def send_email():
    message1=request.form['message']
    password1=request.form['pass']
    server= smtplib.SMTP('smtp.gmail.com')
    sender_email='zengel1706@gmail.com'
    reciever_email=request.form["Email"]
    password=request.form['pass']
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,message1)
    server.quit()
    return render_template('success.html')





if __name__=='__main__':
    app.run(debug=True)

"""--------------Tapelo code Below--------------------"""

