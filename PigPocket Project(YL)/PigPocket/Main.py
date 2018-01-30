from flask import Flask, render_template, request, flash, redirect, url_for,session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField,validators
import datetime
import MainProcess
import tkinter
import tkinter.messagebox
import RetrievingProcess

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    session['userid']="Steven"
    return render_template('home.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')


@app.route('/fundTransfer',methods=['GET',"POST"])
def fundtransfer():
    class newTransaction(Form):
        transaction_details = StringField("Recipient's name:",[validators.Length(min=1, max=150), validators.DataRequired()])
        userlist = []
        user_file = open("file/" + session['userid'].capitalize() , 'r')
        for ulist in user_file:
            list = ulist.split(',')
            if list[2]=="fixed deposit":
                pass
            else:
                s =list[0] + " " + list[2] + " " + list[1]
                userlist.append(s)

        if len(userlist) == 0:
            bank_details = SelectField('Bank Details:', [validators.DataRequired()],choices=[('', 'Select'), ("No accounts", "No accounts")], default='')

        elif len(userlist) == 1:
            bank_details = SelectField('Bank Details:', [validators.DataRequired()],choices=[('', 'Select'), (userlist[0], userlist[0])], default='')

        elif len(userlist) == 2:
            bank_details = SelectField('Bank Details:', [validators.DataRequired()],choices=[('', 'Select'), (userlist[0], userlist[0]), (userlist[1], userlist[1])],default='')

        elif len(userlist) == 3:
            bank_details = SelectField('Bank Details:', [validators.DataRequired()],choices=[('', 'Select'), (userlist[0], userlist[0]), (userlist[1], userlist[1]),(userlist[2], userlist[2])], default='')

        elif len(userlist) == 4:
            bank_details = SelectField('Bank Details:', [validators.DataRequired()],choices=[('', 'Select'), (userlist[0], userlist[0]), (userlist[1], userlist[1]),(userlist[2], userlist[2]), (userlist[3], userlist[3])], default='')

        withdraw = StringField("Amount:", [validators.Length(min=1, max=150), validators.DataRequired()])
        account_type = SelectField('Account Type:', [validators.DataRequired()],choices=[('', 'Select'), ("Posb", "Posb"), ("Ocbc", "Ocbc"), ("Uob", "Uob"),("Maybank", "Maybank")], default='')
        account_number = StringField("Account number(Please omit dash):",[validators.Length(min=1, max=150), validators.DataRequired()])

    form = newTransaction(request.form)
    prev = datetime.datetime.now()
    prevmonth = prev.month-1
    if prevmonth == 0:
        prevmonth = "Dec " + str(prev.year - 1)
    elif prevmonth == 1:
        prevmonth = "Jan " + str(prev.year)
    elif prevmonth == 2:
        prevmonth = "Feb " + str(prev.year)
    elif prevmonth == 3:
        prevmonth = "Mar" + " "  + str(prev.year)
    elif prevmonth == 4:
        prevmonth = "Apr" + " " + str(prev.year)
    elif prevmonth == 5:
        prevmonth = "May " + str(prev.year)
    now = datetime.datetime.now()
    month = now.month
    if month == 1:
        month = "Jan " + str(now.year)
    elif month == 2:
        month = "Feb " + str(now.year)
    elif month == 3:
        month = "Mar " + str(now.year)
    elif month==4:
        month="Apr " + str(now.year)
    elif month==5:
        month="May " + str(now.year)
    todaydate = str(now.day) + " " + month
    if request.method == 'POST' and form.validate():
        try:
            detailsList = []
            user_file = open('file/' + session['userid'].capitalize(), 'r')
            for dlist in user_file:
                list = dlist.split(',')
                s = float(list[5])
                detailsList.append(s)
            float(form.withdraw.data)
            if float(form.withdraw.data)>0:
                if (form.account_number.data.isdigit()):
                    if len(form.withdraw.data.rsplit(".")[-1])==2:
                        if form.bank_details.data.endswith("010-4-444444"):
                            if float(form.withdraw.data)<=detailsList[0]:
                                class Password:
                                    def __init__(self):
                                        self.main_window = tkinter.Tk()
                                        self.top_frame = tkinter.Frame(self.main_window)
                                        self.bottom_frame = tkinter.Frame(self.main_window)
                                        self.label = tkinter.Label(self.top_frame, text="Enter your password: ")
                                        self.entry = tkinter.Entry(self.top_frame, width=10)
                                        self.button = tkinter.Button(self.bottom_frame, text="Enter",
                                                                     command=self.convert)
                                        self.value = tkinter.StringVar()
                                        self.miles = tkinter.Label(self.bottom_frame, textvariable=self.value)

                                        self.button.pack(side='left')
                                        self.miles.pack(side='left')
                                        self.label.pack(side='left')
                                        self.entry.pack(side='left')
                                        self.top_frame.pack()
                                        self.bottom_frame.pack()

                                        tkinter.mainloop()

                                    def convert(self):
                                        pw = self.entry.get()
                                        if pw == "55776688G":
                                            self.value.set("Correct Password")
                                            MainProcess.newTransaction(session["userid"], todaydate,form.bank_details.data,form.transaction_details.data, "None",form.withdraw.data)
                                            tkinter.messagebox.showinfo("Success","You have just transfer $%.2f from %s" % (float(form.withdraw.data),form.bank_details.data))
                                            return "Correct password"

                                        else:
                                            self.value.set("Wrong Password")

                                password = Password()

                            else:
                                tkinter.messagebox.showerror("ALERT","Withdraw amount($%0.2f) is more than account balance($%0.2f)." %(float(form.withdraw.data), detailsList[0]))
                        else:
                            if form.bank_details.data.endswith("010-1-111111"):
                                if float(form.withdraw.data) <= detailsList[1]:
                                    class Password:
                                        def __init__(self):
                                            self.main_window = tkinter.Tk()
                                            self.top_frame = tkinter.Frame(self.main_window)
                                            self.bottom_frame = tkinter.Frame(self.main_window)
                                            self.label = tkinter.Label(self.top_frame, text="Enter your password: ")
                                            self.entry = tkinter.Entry(self.top_frame, width=10)
                                            self.button = tkinter.Button(self.bottom_frame, text="Enter",
                                                                         command=self.convert)
                                            self.value = tkinter.StringVar()
                                            self.miles = tkinter.Label(self.bottom_frame, textvariable=self.value)

                                            self.button.pack(side='left')
                                            self.miles.pack(side='left')
                                            self.label.pack(side='left')
                                            self.entry.pack(side='left')
                                            self.top_frame.pack()
                                            self.bottom_frame.pack()

                                            tkinter.mainloop()

                                        def convert(self):
                                            pw = self.entry.get()
                                            if pw == "55776688G":
                                                self.value.set("Correct Password")
                                                MainProcess.newTransaction(session["userid"], todaydate,
                                                                           form.bank_details.data,
                                                                           form.transaction_details.data, "None",
                                                                           form.withdraw.data)
                                                tkinter.messagebox.showinfo("Success",
                                                                            "You have just transfer $%.2f from %s" % (
                                                                            float(form.withdraw.data),
                                                                            form.bank_details.data))
                                                return "Correct password"

                                            else:
                                                self.value.set("Wrong Password")

                                    password = Password()
                                else:
                                    tkinter.messagebox.showerror("ALERT","Withdraw amount($%0.2f) is more than account balance($%0.2f)."%(float(form.withdraw.data),detailsList[1]))
                            else:
                                if form.bank_details.data.endswith("550-10-89550"):
                                    if float(form.withdraw.data) <= detailsList[2]:
                                        class Password:
                                            def __init__(self):
                                                self.main_window = tkinter.Tk()
                                                self.top_frame = tkinter.Frame(self.main_window)
                                                self.bottom_frame = tkinter.Frame(self.main_window)
                                                self.label = tkinter.Label(self.top_frame, text="Enter your password: ")
                                                self.entry = tkinter.Entry(self.top_frame, width=10)
                                                self.button = tkinter.Button(self.bottom_frame, text="Enter",
                                                                             command=self.convert)
                                                self.value = tkinter.StringVar()
                                                self.miles = tkinter.Label(self.bottom_frame, textvariable=self.value)

                                                self.button.pack(side='left')
                                                self.miles.pack(side='left')
                                                self.label.pack(side='left')
                                                self.entry.pack(side='left')
                                                self.top_frame.pack()
                                                self.bottom_frame.pack()

                                                tkinter.mainloop()

                                            def convert(self):
                                                pw = self.entry.get()
                                                if pw == "55776688G":
                                                    self.value.set("Correct Password")
                                                    MainProcess.newTransaction(session["userid"], todaydate,
                                                                               form.bank_details.data,
                                                                               form.transaction_details.data, "None",
                                                                               form.withdraw.data)
                                                    tkinter.messagebox.showinfo("Success",
                                                                                "You have just transfer $%.2f from %s" % (
                                                                                float(form.withdraw.data),
                                                                                form.bank_details.data))
                                                    return "Correct password"

                                                else:
                                                    self.value.set("Wrong Password")

                                        password = Password()
                                    else:
                                        tkinter.messagebox.showerror("ALERT","Withdraw amount($%0.2f) is more than account balance($%0.2f)." %(float(form.withdraw.data), detailsList[2]))
                                else:
                                    if form.bank_details.data.endswith("910-20-31012"):
                                        if float(form.withdraw.data) <= detailsList[0]:
                                            class Password:
                                                def __init__(self):
                                                    self.main_window = tkinter.Tk()
                                                    self.top_frame = tkinter.Frame(self.main_window)
                                                    self.bottom_frame = tkinter.Frame(self.main_window)
                                                    self.label = tkinter.Label(self.top_frame,
                                                                               text="Enter your password: ")
                                                    self.entry = tkinter.Entry(self.top_frame, width=10)
                                                    self.button = tkinter.Button(self.bottom_frame, text="Enter",
                                                                                 command=self.convert)
                                                    self.value = tkinter.StringVar()
                                                    self.miles = tkinter.Label(self.bottom_frame,
                                                                               textvariable=self.value)

                                                    self.button.pack(side='left')
                                                    self.miles.pack(side='left')
                                                    self.label.pack(side='left')
                                                    self.entry.pack(side='left')
                                                    self.top_frame.pack()
                                                    self.bottom_frame.pack()

                                                    tkinter.mainloop()

                                                def convert(self):
                                                    pw = self.entry.get()
                                                    if pw == "99778800Z":
                                                        self.value.set("Correct Password")
                                                        MainProcess.newTransaction(session["userid"], todaydate,
                                                                                   form.bank_details.data,
                                                                                   form.transaction_details.data,
                                                                                   "None", form.withdraw.data)
                                                        tkinter.messagebox.showinfo("Success",
                                                                                    "You have just transfer $%.2f from %s" % (
                                                                                    float(form.withdraw.data),
                                                                                    form.bank_details.data))
                                                        return "Correct password"

                                                    else:
                                                        self.value.set("Wrong Password")

                                            password = Password()
                                        else:
                                            tkinter.messagebox.showerror("ALERT","Withdraw amount($%0.2f) is more than account balance($%0.2f)." %(float(form.withdraw.data), detailsList[0]))
                    else:
                        tkinter.messagebox.showerror("ALERT","Amount must be in 2 decimal places.")
                else:
                    tkinter.messagebox.showerror("ALERT","Account number only contain numbers.")
            else:
                tkinter.messagebox.showerror("ALERT", "Amount cannot be less than 0")
        except ValueError:
            tkinter.messagebox.showerror("ALERT", "Invalid fund transfer amount")
    userlist = MainProcess.ProcessTransaction(session["userid"])
    totald = float("{0:.2f}".format(MainProcess.Totalamount(session["userid"],"Deposit")))
    totalw = float("{0:.2f}".format(MainProcess.Totalamount(session['userid'],"Withdraw")))
    totalmonthdeposit=float("{0:.2f}".format(MainProcess.CurrentTransaction(session['userid'],month,"Deposit")))
    totalmonthwithdraw = float("{0:.2f}".format(MainProcess.CurrentTransaction(session['userid'], month, "Withdraw")))
    totalprevdeposit = float("{0:.2f}".format(MainProcess.CurrentTransaction(session['userid'], prevmonth, "Deposit")))
    totalprevwithdraw = float("{0:.2f}".format(MainProcess.CurrentTransaction(session['userid'], prevmonth, "Withdraw")))
    detailsList = RetrievingProcess.processUserDetails(session['userid'])
    return render_template('fundtransfer.html',totalw=totalw,totald=totald,Transaction=userlist,form=form,totalmonthdeposit=totalmonthdeposit,totalmonthwithdraw=totalmonthwithdraw,totalprevwithdraw=totalprevwithdraw,totalprevdeposit=totalprevdeposit,month=month,detailsList=detailsList)

@app.route('/giro')
def giro():
    return render_template('giro.html')

@app.route('/spendinganalytics')
def spendinganalytics():
    prev = datetime.datetime.now()
    prevmonth = prev.month-1
    if prevmonth==0:
        prevmonth="Dec "+ str(prev.year-1)
    elif prevmonth==1:
        prevmonth="Jan "+ str(prev.year)
    elif prevmonth==2:
        prevmonth="Feb "+ str(prev.year)
    elif prevmonth==3:
        prevmonth="Mar "+ str(prev.year)
    elif prevmonth==4:
        prevmonth="Apr "+ str(prev.year)
    elif prevmonth==5:
        prevmonth="May "+ str(prev.year)
    now = datetime.datetime.now()
    month=now.month
    if month==1:
        month="Jan " + str(now.year)
    elif month==2:
        month="Feb " + str(now.year)
    elif month==3:
        month="Mar" + " " + str(now.year)
    elif month==4:
        month="Apr" + " " + str(now.year)
    elif month==5:
        month="May " + str(now.year)
    totalprevdeposit = MainProcess.CurrentTransaction(session["userid"],prevmonth,"Deposit")
    totalprevwithdraw = MainProcess.CurrentTransaction(session["userid"], prevmonth, "Withdraw")
    totaldeposit=MainProcess.CurrentTransaction(session["userid"],month,"Deposit")
    totalwithdraw=MainProcess.CurrentTransaction(session["userid"],month,"Withdraw")
    depositdifference = float("{0:.2f}".format(totaldeposit - totalwithdraw))
    withdrawdifference = float("{0:.2f}".format(totalwithdraw - totaldeposit))
    return render_template('spendinganalytics.html',totalprevdeposit=totalprevdeposit,totalprevwithdraw=totalprevwithdraw,totaldeposit=totaldeposit,totalwithdraw=totalwithdraw,depositdifference=depositdifference,withdrawdifference=withdrawdifference,prevmonth=prevmonth,month=month)

@app.route("/transaction")
def transaction():
    list = MainProcess.ProcessTransaction(session["userid"])
    prev = datetime.datetime.now()
    prevmonth = prev.month - 1
    if prevmonth == 0:
        prevmonth = "Dec" + " " + str(prev.year - 1)
    elif prevmonth == 1:
        prevmonth = "Jan " + str(prev.year)
    elif prevmonth == 2:
        prevmonth = "Feb " + str(prev.year)
    elif prevmonth == 3:
        prevmonth = "Mar " + str(prev.year)
    elif prevmonth == 4:
        prevmonth = "Apr " + str(prev.year)
    elif prevmonth == 5:
        prevmonth = "May " + str(prev.year)
    now = datetime.datetime.now()
    month = now.month
    if month == 1:
        month = "Jan " + str(now.year)
    elif month == 2:
        month = "Feb " + str(now.year)
    elif month == 3:
        month = "Mar " + str(now.year)
    elif month==4:
        month="Apr " + str(now.year)
    elif month==5:
        month="May " + str(now.year)
    totalprevdeposit = float("{0:.2f}".format(MainProcess.CurrentTransaction(session["userid"],prevmonth,"Deposit")))
    totalprevwithdraw = float("{0:.2f}".format(MainProcess.CurrentTransaction(session["userid"], prevmonth, "Withdraw")))
    totaldeposit=float("{0:.2f}".format(MainProcess.CurrentTransaction(session["userid"],month,"Deposit")))
    totalwithdraw=float("{0:.2f}".format(MainProcess.CurrentTransaction(session["userid"],month,"Withdraw")))
    return render_template("transaction.html",Transaction=list,totalprevdeposit=totalprevdeposit,totalprevwithdraw=totalprevwithdraw,totaldeposit=totaldeposit,totalwithdraw=totalwithdraw,month=month,prevmonth=prevmonth)

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
