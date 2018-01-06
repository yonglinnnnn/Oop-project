from flask import Flask, render_template, request, flash, redirect, url_for,session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField,validators
import datetime
import MainProcess
import tkinter

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
    session['userid'] = 'Audrey'
    form = newTransaction(request.form)
    if request.method == 'POST' and form.validate():
        now=datetime.datetime.now()
        todaydate=str(now.day)+ " " + "Jan" + " " + str(now.year)
        try:
            float(form.withdraw.data)
            if float(form.withdraw.data)>0:
                MainProcess.newTransaction(session["userid"],todaydate,form.bank_details.data,form.transaction_details.data,"None",form.withdraw.data)
            else:
                class HelloGUI:
                    def __init__(self):
                        self.main_window = tkinter.Tk()
                        self.label = tkinter.Label(self.main_window, text="Invalid Transfer Amount")
                        self.label.pack()
                        tkinter.mainloop()
                gui = HelloGUI()
        except ValueError:
            class HelloGUI:
                def __init__(self):
                    self.main_window=tkinter.Tk()
                    self.label=tkinter.Label(self.main_window,text="Invalid Transfer Amount")
                    self.label.pack()
                    tkinter.mainloop()
            gui=HelloGUI()
    userlist=MainProcess.processTransaction(session["userid"])
    totalprevdeposit=MainProcess.CurrentTransaction(session["userid"],"Dec","Deposit")
    totaldeposit=MainProcess.CurrentTransaction(session['userid'],"Jan","Deposit")
    totalprevwithdraw=MainProcess.CurrentTransaction(session['userid'],"Dec","Withdraw")
    totalwithdraw=MainProcess.CurrentTransaction(session['userid'],"Jan","Withdraw")
    totald=totalprevdeposit+totaldeposit
    totalw=totalwithdraw+totalprevwithdraw
    return render_template('fundtransfer.html',Transaction=userlist,form=form,totaldeposit=totald,totalwithdraw=totalw)

@app.route('/giro')
def giro():
    return render_template('giro.html')

@app.route('/spendinganalytics')
def spendinganalytics():
    session['userid']="Audrey"
    totalprevdeposit = MainProcess.CurrentTransaction(session["userid"],"Dec","Deposit")
    totalprevwithdraw = MainProcess.CurrentTransaction(session["userid"], "Dec", "Withdraw")
    totaldeposit=MainProcess.CurrentTransaction(session["userid"],"Jan","Deposit")
    totalwithdraw=MainProcess.CurrentTransaction(session["userid"],"Jan","Withdraw")
    return render_template('spendinganalytics.html',totalprevdeposit=totalprevdeposit,totalprevwithdraw=totalprevwithdraw,totaldeposit=totaldeposit,totalwithdraw=totalwithdraw)

@app.route("/transaction")
def transaction():
    session['userid'] = 'Audrey'
    list = MainProcess.processTransaction(session["userid"])
    totalprevdeposit = MainProcess.CurrentTransaction(session["userid"],"Dec","Deposit")
    totalprevwithdraw = MainProcess.CurrentTransaction(session["userid"], "Dec", "Withdraw")
    totaldeposit=MainProcess.CurrentTransaction(session["userid"],"Jan","Deposit")
    totalwithdraw=MainProcess.CurrentTransaction(session["userid"],"Jan","Withdraw")
    return render_template("transaction.html",Transaction=list,totalprevdeposit=totalprevdeposit,totalprevwithdraw=totalprevwithdraw,totaldeposit=totaldeposit,totalwithdraw=totalwithdraw)

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
