from flask import Flask, render_template, request, flash, redirect, url_for,session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField,validators

import MainProcess

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

class newTransaction(Form):
    transaction_details = StringField("Recipient's name:", [validators.Length(min=1, max=150), validators.DataRequired()])
    bank_details = SelectField('Bank Details:', [validators.DataRequired()],choices=[('', 'Select'), ("Posb 130-48734-9","Posb 130-48734-9"),("Ocbc 613-54986-9","Ocbc 613-54986-9")],default='')
    withdraw = StringField("Amount:", [validators.Length(min=1, max=150), validators.DataRequired()])
    account_type = SelectField('Account Type:', [validators.DataRequired()],choices=[('', 'Select'), ("Posb","Posb"),("Ocbc","Ocbc"),("Uob","Uob"),("Maybank","Maybank")],default='')
    account_number = StringField("Account number:",[validators.Length(min=1, max=150), validators.DataRequired()])

@app.route('/fundTransfer',methods=['GET',"POST"])
def fundtransfer():
    session['name'] = 'Yonglin'
    form = newTransaction(request.form)
    if request.method == 'POST' and form.validate():
        MainProcess.newTransaction(session["name"],"31 Dec 2017",form.bank_details.data,form.transaction_details.data,"None",form.withdraw.data)
    userlist=[]
    userlist=MainProcess.processTransaction()
    return render_template('fundtransfer.html',Transaction=userlist,form=form)

@app.route('/giro')
def giro():
    return render_template('giro.html')

@app.route('/spendinganalytics')
def spendinganalytics():
    return render_template('spendinganalytics.html')

@app.route("/transaction")
def transaction():
    return render_template("transaction.html")

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
