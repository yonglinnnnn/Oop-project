from flask import Flask, render_template, request, flash, redirect, url_for,session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField,validators
import datetime
import MainProcess
import processpoint
import tkinter
import tkinter.messagebox
import RetrievingProcess
import ProcessBankTrans
import processBankPromo
import UpdatingProcess
from datetime import date
from newgiro import NewGiroUser

app = Flask(__name__)

class LoginUser(Form):
    userId = StringField('SingPass ID', [validators.Length(min=9, max=10), validators.DataRequired()])
    userPass = StringField('SingPass Password', [validators.Length(min=8, max=24), validators.DataRequired()])

@app.route('/', methods = ["GET","POST"])
def root():

    form = LoginUser(request.form)
    if request.method == "POST" and form.validate():
        userList=MainProcess.loginUser()
        for i in userList:
                if form.userId.data==i.get_nric():
                    if form.userPass.data==i.get_password():

                        session["userid"] = i.get_name()

                        now = datetime.datetime.now()
                        month = now.month
                        year = now.year
                        date = str(now.day) + "-" + str(now.month) + "-" + str(now.year)

                        prev_month = now.month - 1
                        prev_year = now.year - 1

                        if month == 1:
                            n_month = "Jan" + " " + str(year)
                        elif month == 2:
                            n_month = "Feb" + " " + str(year)
                        elif month == 3:
                            n_month = "Mar" + " " + str(year)
                        elif month == 4:
                            n_month = "Apr" + " " + str(year)
                        elif month == 5:
                            n_month = "May" + " " + str(year)
                        elif month == 6:
                            n_month = "Jun" + " " + str(year)
                        elif month == 7:
                            n_month = "Jul" + " " + str(year)
                        elif month == 8:
                            n_month = "Aug" + " " + str(year)
                        elif month == 9:
                            n_month = "Sep" + " " + str(year)
                        elif month == 10:
                            n_month = "Oct" + " " + str(year)
                        elif month == 11:
                            n_month = "Nov" + " " + str(year)
                        elif month == 12:
                            n_month = "Dec" + " " + str(year)


                        if prev_month == 0:
                            prev_month = "Dec" + " " + str(prev_year)
                        elif prev_month == 1:
                            prev_month = "Jan" + " " + str(year)
                        elif prev_month == 2:
                            prev_month = "Feb" + " " + str(year)
                        elif prev_month == 3:
                            prev_month = "Mar" + " " + str(year)
                        elif prev_month == 4:
                            prev_month = "Apr" + " " + str(year)
                        elif prev_month == 5:
                            prev_month = "May" + " " + str(year)
                        elif prev_month == 6:
                            prev_month = "Jun" + " " + str(year)
                        elif prev_month == 7:
                            prev_month = "Jul" + " " + str(year)
                        elif prev_month == 8:
                            prev_month = "Aug" + " " + str(year)
                        elif prev_month == 9:
                            prev_month = "Sep" + " " + str(year)
                        elif prev_month == 10:
                            prev_month = "Oct" + " " + str(year)
                        elif prev_month == 11:
                            prev_month = "Nov" + " " + str(year)


                        points = int(MainProcess.get_points(session["userid"]))

                        hi = int(MainProcess.get_points(session["userid"]))

                        count = MainProcess.get_fd(session['userid'])

                        statusday = MainProcess.get_status_day(session["userid"])

                        statusmonth = MainProcess.get_status_month(session["userid"])

                        statusyear = MainProcess.get_status_year(session["userid"])

                        account = MainProcess.fd_table(session['userid'])

                        tsa = MainProcess.s_balance(session["userid"],"savings")

                        tsc = MainProcess.s_balance(session["userid"],"current")

                        totaldeposit = 0
                        totalwithdrawal = 0
                        totalsavings = 0
                        totalcurrent = 0
                        totalfixed = 0

                        totaldeposit = MainProcess.deposits(session['userid'], n_month)
                        totalwithdrawal = MainProcess.spendings(session['userid'], n_month)
                        totalsavings = MainProcess.savings(session['userid'], n_month, "savings")
                        totalcurrent = MainProcess.current(session['userid'], n_month, "current")
                        totalfixed = MainProcess.processFixedDeposit(session['userid'], 'fixed deposit')

                        p_totaldeposit = MainProcess.deposits(session['userid'], prev_month)
                        p_totalwithdrawal = MainProcess.spendings(session['userid'], prev_month)
                        p_totalsavings = MainProcess.savings(session['userid'], prev_month, "savings")
                        p_totalcurrent = MainProcess.current(session['userid'], prev_month, "current")
                        p_totalfixed = MainProcess.processFixedDeposit(session['userid'], 'fixed deposit')


                        return render_template('home.html',account=account, count=count, totalda=totaldeposit, totalwa=totalwithdrawal
                                               ,totalsa=totalsavings, totalca=totalcurrent, totalfd=totalfixed, p_totalda=p_totaldeposit
                                               , p_totalwa=p_totalwithdrawal,p_totalsa=p_totalsavings, p_totalca=p_totalcurrent
                                               , p_totalfd=p_totalfixed, userid = session["userid"], points=points, n_month=n_month
                                               , prev_month=prev_month, date=date, statusday=statusday, statusmonth=statusmonth
                                               , statusyear=statusyear, tsa=tsa, tsc=tsc,hi=hi)
                    else:
                        flash("Invalid Information")
                        return redirect("/")


    return render_template('login.html',form=form)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    date = str(now.day) + "-" + str(now.month) + "-" + str(now.year)

    prev_month = now.month - 1
    prev_year = now.year - 1

    if month == 1:
        n_month = "Jan" + " " + str(year)
    elif month == 2:
        n_month = "Feb" + " " + str(year)
    elif month == 3:
        n_month = "Mar" + " " + str(year)
    elif month == 4:
        n_month = "Apr" + " " + str(year)
    elif month == 5:
        n_month = "May" + " " + str(year)
    elif month == 6:
        n_month = "Jun" + " " + str(year)
    elif month == 7:
        n_month = "Jul" + " " + str(year)
    elif month == 8:
        n_month = "Aug" + " " + str(year)
    elif month == 9:
        n_month = "Sep" + " " + str(year)
    elif month == 10:
        n_month = "Oct" + " " + str(year)
    elif month == 11:
        n_month = "Nov" + " " + str(year)
    elif month == 12:
        n_month = "Dec" + " " + str(year)

    if prev_month == 0:
        prev_month = "Dec" + " " + str(prev_year)
    elif prev_month == 1:
        prev_month = "Jan" + " " + str(year)
    elif prev_month == 2:
        prev_month = "Feb" + " " + str(year)
    elif prev_month == 3:
        prev_month = "Mar" + " " + str(year)
    elif prev_month == 4:
        prev_month = "Apr" + " " + str(year)
    elif prev_month == 5:
        prev_month = "May" + " " + str(year)
    elif prev_month == 6:
        prev_month = "Jun" + " " + str(year)
    elif prev_month == 7:
        prev_month = "Jul" + " " + str(year)
    elif prev_month == 8:
        prev_month = "Aug" + " " + str(year)
    elif prev_month == 9:
        prev_month = "Sep" + " " + str(year)
    elif prev_month == 10:
        prev_month = "Oct" + " " + str(year)
    elif prev_month == 11:
        prev_month = "Nov" + " " + str(year)

    points = int(MainProcess.get_points(session["userid"]))

    hi = int(MainProcess.get_points(session["userid"]))

    count = MainProcess.get_fd(session['userid'])

    statusday = MainProcess.get_status_day(session["userid"])

    statusmonth = MainProcess.get_status_month(session["userid"])

    statusyear = MainProcess.get_status_year(session["userid"])

    account = MainProcess.fd_table(session['userid'])

    tsa = MainProcess.s_balance(session["userid"], "savings")

    tsc = MainProcess.s_balance(session["userid"], "current")

    totaldeposit = 0
    totalwithdrawal = 0
    totalsavings = 0
    totalcurrent = 0
    totalfixed = 0

    totaldeposit = MainProcess.deposits(session['userid'], n_month)
    totalwithdrawal = MainProcess.spendings(session['userid'], n_month)
    totalsavings = MainProcess.savings(session['userid'], n_month, "savings")
    totalcurrent = MainProcess.current(session['userid'], n_month, "current")
    totalfixed = MainProcess.processFixedDeposit(session['userid'], 'fixed deposit')

    p_totaldeposit = MainProcess.deposits(session['userid'], prev_month)
    p_totalwithdrawal = MainProcess.spendings(session['userid'], prev_month)
    p_totalsavings = MainProcess.savings(session['userid'], prev_month, "savings")
    p_totalcurrent = MainProcess.current(session['userid'], prev_month, "current")
    p_totalfixed = MainProcess.processFixedDeposit(session['userid'], 'fixed deposit')

    return render_template('home.html', account=account, count=count, totalda=totaldeposit, totalwa=totalwithdrawal
                           , totalsa=totalsavings, totalca=totalcurrent, totalfd=totalfixed, p_totalda=p_totaldeposit
                           , p_totalwa=p_totalwithdrawal, p_totalsa=p_totalsavings, p_totalca=p_totalcurrent
                           , p_totalfd=p_totalfixed, userid=session["userid"], points=points, n_month=n_month
                           , prev_month=prev_month, date=date, statusday=statusday, statusmonth=statusmonth
                           , statusyear=statusyear, tsa=tsa, tsc=tsc, hi=hi)



@app.route('/accounts')
def accounts():
    xxx_x_444444 = ""
    xxx_x_444444_totalWithdrawal = ""
    xxx_x_444444_totalDeposit = ""
    prev_xxx_x_444444 = ""
    prev_xxx_x_444444_totalWithdrawal = ""
    prev_xxx_x_444444_totalDeposit = ""

    xxx_x_111111 = ""
    xxx_x_111111_totalWithdrawal = ""
    xxx_x_111111_totalDeposit = ""
    prev_xxx_x_111111 = ""
    prev_xxx_x_111111_totalWithdrawal = ""
    prev_xxx_x_111111_totalDeposit = ""

    xxx_xx_89550 = ""
    xxx_xx_89550_totalWithdrawal = ""
    xxx_xx_89550_totalDeposit = ""
    prev_xxx_xx_89550 = ""
    prev_xxx_xx_89550_totalWithdrawal = ""
    prev_xxx_xx_89550_totalDeposit = ""

    xxx_xx_31012 = ""
    xxx_xx_31012_totalWithdrawal = ""
    xxx_xx_31012_totalDeposit = ""
    prev_xxx_xx_31012 = ""
    prev_xxx_xx_31012_totalWithdrawal = ""
    prev_xxx_xx_31012_totalDeposit = ""

    # took from yonglin's part
    prev = datetime.datetime.now()
    prevmonth = prev.month - 1
    prevYear = ""
    if prevmonth == 0:
        prevmonth = "Dec"
        prevYear = str(prev.year - 1)
    elif prevmonth == 1:
        prevmonth = "Jan"
        prevYear = str(prev.year)
    elif prevmonth == 2:
        prevmonth = "Feb"
        prevYear = str(prev.year)
    elif prevmonth == 3:
        prevmonth = "Mar"
        prevYear = str(prev.year)
    elif prevmonth == 4:
        prevmonth = "Apr"
        prevYear = str(prev.year)
    elif prevmonth == 5:
        prevmonth = "May"
        prevYear = str(prev.year)
    elif prevmonth == 6:
        prevmonth = "Jun"
        prevYear = str(prev.year)
    elif prevmonth == 7:
        prevmonth = "Jul"
        prevYear = str(prev.year)
    elif prevmonth == 8:
        prevmonth = "Aug"
        prevYear = str(prev.year)
    elif prevmonth == 9:
        prevmonth = "Sep"
        prevYear = str(prev.year)
    elif prevmonth == 10:
        prevmonth = "Oct"
        prevYear = str(prev.year)
    elif prevmonth == 11:
        prevmonth = "Nov"
        prevYear = str(prev.year)
    elif prevmonth == 12:
        prevmonth = "Dec"
        prevYear = str(prev.year)
    ###########################################

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthNowInt = datetime.datetime.now().month - 1

    dayNow = datetime.date.today().strftime("%d")
    monthNow = datetime.date.today().strftime("%B")
    yearNow = datetime.date.today().strftime("%Y")
    detailsList = RetrievingProcess.processUserDetails(session['userid'])
    fixedDepositList_length = len(detailsList)
    branchesList = RetrievingProcess.processBankBranches(session['userid'])
    typesList = RetrievingProcess.processBankType(session['userid'])
    if session['userid'] == "Steven":
        xxx_x_444444 = ProcessBankTrans.process_accountTransaction("010-4-444444", months[monthNowInt], yearNow)
        xxx_x_444444_totalWithdrawal = RetrievingProcess.processWithdrawal('010-4-444444', months[monthNowInt], yearNow)
        xxx_x_444444_totalDeposit = RetrievingProcess.processDeposit('010-4-444444', months[monthNowInt], yearNow)
        prev_xxx_x_444444 = ProcessBankTrans.process_accountTransaction("010-4-444444", prevmonth, prevYear)
        prev_xxx_x_444444_totalWithdrawal = RetrievingProcess.processWithdrawal('010-4-444444', prevmonth, prevYear)
        prev_xxx_x_444444_totalDeposit = RetrievingProcess.processDeposit('010-4-444444', prevmonth, prevYear)

        xxx_x_111111 = ProcessBankTrans.process_accountTransaction("010-1-111111", months[monthNowInt], yearNow)
        xxx_x_111111_totalWithdrawal = RetrievingProcess.processWithdrawal('010-1-111111', months[monthNowInt], yearNow)
        xxx_x_111111_totalDeposit = RetrievingProcess.processDeposit('010-1-111111', months[monthNowInt], yearNow)
        prev_xxx_x_111111 = ProcessBankTrans.process_accountTransaction("010-1-111111", prevmonth, prevYear)
        prev_xxx_x_111111_totalWithdrawal = RetrievingProcess.processWithdrawal('010-1-111111', prevmonth, prevYear)
        prev_xxx_x_111111_totalDeposit = RetrievingProcess.processDeposit('010-1-111111', prevmonth, prevYear)

        xxx_xx_89550 = ProcessBankTrans.process_accountTransaction("550-10-89550", months[monthNowInt], yearNow)
        xxx_xx_89550_totalWithdrawal = RetrievingProcess.processWithdrawal('010-1-111111', months[monthNowInt], yearNow)
        xxx_xx_89550_totalDeposit = RetrievingProcess.processDeposit('010-1-111111', months[monthNowInt], yearNow)
        prev_xxx_xx_89550 = ProcessBankTrans.process_accountTransaction("550-10-89550", prevmonth, prevYear)
        prev_xxx_xx_89550_totalWithdrawal = RetrievingProcess.processWithdrawal('010-1-111111', prevmonth, prevYear)
        prev_xxx_xx_89550_totalDeposit = RetrievingProcess.processDeposit('010-1-111111', prevmonth, prevYear)

    elif session['userid'] == 'Kelly':
        xxx_xx_31012 = ProcessBankTrans.process_accountTransaction("910-20-31012", months[monthNowInt], yearNow)
        xxx_xx_31012_totalWithdrawal = RetrievingProcess.processWithdrawal('910-20-31012', months[monthNowInt], yearNow)
        xxx_xx_31012_totalDeposit = RetrievingProcess.processDeposit('910-20-31012', months[monthNowInt], yearNow)
        prev_xxx_xx_31012 = ProcessBankTrans.process_accountTransaction("910-20-31012", prevmonth, prevYear)
        prev_xxx_xx_31012_totalWithdrawal = RetrievingProcess.processWithdrawal('910-20-31012', prevmonth, prevYear)
        prev_xxx_xx_31012_totalDeposit = RetrievingProcess.processDeposit('910-20-31012', prevmonth, prevYear)

    dbs_savingPromos = processBankPromo.processBankPromo('dbs', 'savings',
                                                         (str(prev.day) + '-' + str(prev.month) + '-' + str(prev.year)))
    ocbc_savingPromos = processBankPromo.processBankPromo('ocbc', 'savings', (
    str(prev.day) + '-' + str(prev.month) + '-' + str(prev.year)))

    return render_template('accounts.html', accounts=detailsList, fixedDepositList_length=fixedDepositList_length,
                           branches=branchesList, types=typesList,
                           transactions=xxx_x_444444, xxx_x_444444_totalWithdrawal=xxx_x_444444_totalWithdrawal,
                           xxx_x_444444_totalDeposit=xxx_x_444444_totalDeposit,
                           prevtransactions=prev_xxx_x_444444,
                           prev_xxx_x_444444_totalWithdrawal=prev_xxx_x_444444_totalWithdrawal,
                           prev_xxx_x_444444_totalDeposit=prev_xxx_x_444444_totalDeposit,
                           transactions2=xxx_x_111111, xxx_x_111111_totalWithdrawal=xxx_x_111111_totalWithdrawal,
                           xxx_x_111111_totalDeposit=xxx_x_111111_totalDeposit,
                           prevtransactions2=prev_xxx_x_111111,
                           prev_xxx_x_111111_totalWithdrawal=prev_xxx_x_111111_totalWithdrawal,
                           prev_xxx_x_111111_totalDeposit=prev_xxx_x_111111_totalDeposit,
                           transactions3=xxx_xx_89550, xxx_xx_89550_totalWithdrawal=xxx_xx_89550_totalWithdrawal,
                           xxx_xx_89550_totalDeposit=xxx_xx_89550_totalDeposit,
                           prevtransactions3=prev_xxx_xx_89550,
                           prev_xxx_xx_89550_totalWithdrawal=prev_xxx_xx_89550_totalWithdrawal,
                           prev_xxx_xx_89550_totalDeposit=prev_xxx_xx_89550_totalDeposit,
                           transactions4=xxx_xx_31012, xxx_xx_31012_totalWithdrawal=xxx_xx_31012_totalWithdrawal,
                           xxx_xx_31012_totalDeposit=xxx_xx_31012_totalDeposit,
                           prevtransactions4=prev_xxx_xx_31012,
                           prev_xxx_xx_31012_totalWithdrawal=prev_xxx_xx_31012_totalWithdrawal,
                           prev_xxx_xx_31012_totalDeposit=prev_xxx_xx_31012_totalDeposit,
                           dayNow=dayNow, monthNow=monthNow, monthNow2=months[monthNowInt], monthPrev=prevmonth,
                           yearNow=yearNow, yearPrev=prevYear,
                           DBSpromoList=dbs_savingPromos, OCBCpromoList=ocbc_savingPromos)
    # duration= duration, principalDate= principalDate, maturedDate= maturedDate, principalAmount= principalAmount, maturedAmount= maturedAmount

    return render_template('accounts.html')


@app.route('/fundTransfer',methods=['GET',"POST"])
def fundtransfer():
    class newTransaction(Form):
        transaction_details = StringField("Recipient's name:",[validators.Length(min=1, max=150), validators.DataRequired()])
        try:
            userlist = []
            user_file = open("file/" + session['userid'].capitalize() , 'r')
            for ulist in user_file:
                list = ulist.split(',')
                if list[2]=="fixed deposit":
                    pass
                else:
                    s =list[0] + " " + list[2] + " " + list[1]
                    userlist.append(s)
        except IOError:
            print("File not found")
        except IndexError:
            print("Index got error")


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
    totald = MainProcess.Totalamount(session["userid"],"Deposit")
    totalw = MainProcess.Totalamount(session['userid'],"Withdraw")
    totalmonthdeposit=MainProcess.CurrentTransaction(session['userid'],month,"Deposit")
    totalmonthwithdraw = MainProcess.CurrentTransaction(session['userid'], month, "Withdraw")
    #totalprevdeposit = MainProcess.CurrentTransaction(session['userid'], prevmonth,"Deposit")
    #totalprevwithdraw = MainProcess.CurrentTransaction(session['userid'], prevmonth,"Withdraw")
    totalprevdeposit = MainProcess.deposits(session["userid"], prevmonth)
    totalprevwithdraw = MainProcess.spendings(session["userid"], prevmonth)
    detailsList = RetrievingProcess.processUserDetails(session['userid'])
    transaction = MainProcess.ProcessTransaction(session["userid"])
    return render_template('fundtransfer.html',transaction=transaction,totalw=totalw,totald=totald,Transaction=userlist,form=form,totalmonthdeposit=totalmonthdeposit,totalmonthwithdraw=totalmonthwithdraw,totalprevwithdraw=totalprevwithdraw,totalprevdeposit=totalprevdeposit,month=month,detailsList=detailsList,prevmonth=prevmonth)

class Girotransaction(Form):
    # name = StringField('Name:')
    bankno = StringField('Bank number:', [validators.Length(min=1, max=12), validators.DataRequired()])
    amount = StringField('Amount Payable:', [validators.Length(min=1, max=100), validators.DataRequired()])
    payto = StringField('Bank Number(pay to):', [validators.Length(min=1, max=12), validators.DataRequired()])
    specify = StringField('Specify:', [validators.Length(min=1, max=100), validators.DataRequired()])
    # date = StringField('Date:', [validators.Length(min=1, max=100), validators.DataRequired()])
    category = SelectField('Category:', [validators.DataRequired()], choices = [('All', 'all'), ('Utilities', 'utility'), ('Bills', 'bills'), ('Standard Transfer', 'standard transfer')])

@app.route('/giro', methods=['GET', "POST"])
def giro():
    form= Girotransaction(request.form)
    today=datetime.datetime.now()
    hi=str(today.year)+"-"+str(today.month) + "-"+ str(today.day)
    prevmonth=today.month
    if request.method =="POST" and form.validate():
        MainProcess.newGiro(session['userid'],form.bankno.data, form.amount.data, form.payto.data, form.specify.data, str(hi) , form.category.data, str(prevmonth) )
        print('success')
    return render_template('giro.html', form=form, newgiro=MainProcess.addUser(session['userid']))


@app.route('/update/<string:postlist>/', methods=['GET', 'POST'])
def update_userDetails(postlist):
    plist = postlist.split('$')
    bankno=plist[0]
    specify=plist[1]
    form= Girotransaction(request.form)

    girolist=MainProcess.addUser(session['userid'])
    girodetails=MainProcess.displaydetails(bankno, specify)
    return render_template('giro.html', form=form, newgiro=girolist,  girodetails=girodetails )

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
    totalprevdeposit = MainProcess.deposits(session["userid"],prevmonth)
    totalprevwithdraw = MainProcess.spendings(session["userid"], prevmonth)
    totaldeposit=float(MainProcess.deposits(session["userid"],month))
    totalwithdraw=float(MainProcess.spendings(session["userid"],month))
    depositdifference = float(totaldeposit) - float(totalwithdraw)
    withdrawdifference = float(totalwithdraw) - float(totaldeposit)
    depositdifference="%0.2f"%depositdifference
    withdrawdifference="%0.2f"%withdrawdifference

    return render_template('spendinganalytics.html',totalprevdeposit=totalprevdeposit,totalprevwithdraw=totalprevwithdraw,totaldeposit=totaldeposit,totalwithdraw=totalwithdraw,depositdifference=depositdifference,withdrawdifference=withdrawdifference,prevmonth=prevmonth,month=month)

@app.route("/transaction",methods=['GET',"POST"])
def transaction():
    class newTransaction(Form):
        month=SelectField('Month', [validators.DataRequired()],choices=[('', 'Select'), ("Jan", "January 2018"),("Feb","February 2018"),("Mar","March 2018"),("Apr","April 2018"),("May","May 2018"),("June","June 2018"),("July","July 2018"),("Aug","August 2018"),("Sep","September 2018"),("Oct","October 2018"),("Nov","November 2018"),("Dec","December 2018")], default='')
        userlist = []
        user_file = open("file/" + session['userid'].capitalize(), 'r')
        for ulist in user_file:
            list = ulist.split(',')
            s = list[0]
            if s not in userlist:
                userlist.append(s)
        if len(userlist)== 0:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'), ("No account", "No account")], default='')
        elif len(userlist)== 1:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'),("All","All"),(userlist[0].lower(), userlist[0])], default='')
        elif len(userlist)== 2:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'),("All","All"), (userlist[0].lower(), userlist[0]),(userlist[1].lower(),userlist[1])], default='')
        elif len(userlist)==3:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'),("All","All"), (userlist[0].lower(), userlist[0]),(userlist[1].lower(),userlist[1]),(userlist[2].lower(),userlist[2])], default='')
        elif len(userlist)==4:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'),("All","All"),(userlist[0].lower(), userlist[0]),(userlist[1].lower(),userlist[1]),(userlist[2].lower(),userlist[2]),(userlist[3].lower(),userlist[3])], default='')
    form = newTransaction(request.form)
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
    elif month == 4:
        month = "Apr " + str(now.year)
    elif month == 5:
        month = "May " + str(now.year)
    prevvmonth = now.month-1
    if prevvmonth == 1:
        prevvmonth = "Jan"
    elif prevvmonth == 2:
        prevvmonth = "Feb"
    elif prevvmonth == 3:
        prevvmonth = "Mar"
    elif prevvmonth == 4:
        prevvmonth = "Apr"
    elif prevvmonth==5:
        prevvmonth="May"
    elif prevvmonth==6:
        prevvmonth="June"
    elif prevvmonth==7:
        prevvmonth="July"
    elif prevvmonth==8:
        prevvmonth="Aug"
    elif prevvmonth==9:
        prevvmonth="Sep"
    elif prevvmonth==10:
        prevvmonth="Oct"
    elif prevvmonth==11:
        prevvmonth="Nov"
    else:
        prevvmonth="Dec"

    justmonth = now.month
    if justmonth == 1:
        justmonth = "Jan"
    elif justmonth == 2:
        justmonth = "Feb"
    elif justmonth == 3:
        justmonth = "Mar"
    elif justmonth == 4:
        justmonth = "Apr"
    elif justmonth==5:
        justmonth="May"
    elif justmonth==6:
        justmonth="June"
    elif justmonth==7:
        justmonth="July"
    elif justmonth==8:
        justmonth="Aug"
    elif justmonth==9:
        justmonth="Sep"
    elif justmonth==10:
        justmonth="Oct"
    elif justmonth==11:
        justmonth="Nov"
    else:
        justmonth="Dec"

    if request.method == 'POST' and form.validate():
        hello=MainProcess.filter(session['userid'],form.bank.data,form.month.data)

    p = form.bank.data
    q = form.month.data
    if p=="":
        p="hi"
    if q=="":
        q="hi"
    hello = MainProcess.filter(session['userid'], form.bank.data, form.month.data)
    plist = MainProcess.spendinganalyticstransaction(session["userid"])
    totalprevdeposit = MainProcess.deposits(session["userid"], prevmonth)
    totalprevwithdraw = MainProcess.spendings(session["userid"], prevmonth)
    totaldeposit = MainProcess.deposits(session["userid"], month)
    totalwithdraw = MainProcess.spendings(session["userid"], month)
    totalforfilterdeposit=MainProcess.totalforfilterdeposit(session["userid"],form.month.data,form.bank.data)
    totalforfilterwithdraw=MainProcess.totalforfilterwithdraw(session['userid'],form.month.data,form.bank.data)
    return render_template("transaction.html",totalforfilterwithdraw=totalforfilterwithdraw,totalforfilterdeposit=totalforfilterdeposit,prevvmonth=prevvmonth,justmonth=justmonth,another=plist,p=p,q=q,Transaction=hello,totalprevdeposit=totalprevdeposit,totalprevwithdraw=totalprevwithdraw,totaldeposit=totaldeposit,totalwithdraw=totalwithdraw,month=month,prevmonth=prevmonth,form=form)

@app.route("/prevtransaction",methods=['GET',"POST"])
def prevtransaction():
    class newTransaction(Form):
        month=SelectField('Month', [validators.DataRequired()],choices=[('', 'Select'), ("Jan", "January 2018"),("Feb","February 2018"),("Mar","March 2018"),("Apr","April 2018"),("May","May 2018"),("June","June 2018"),("July","July 2018"),("Aug","August 2018"),("Sep","September 2018"),("Oct","October 2018"),("Nov","November 2018"),("Dec","December 2018")], default='')
        userlist = []
        user_file = open("file/" + session['userid'].capitalize(), 'r')
        for ulist in user_file:
            list = ulist.split(',')
            s = list[0]
            if s not in userlist:
                userlist.append(s)
        if len(userlist)== 0:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'), ("No account", "No account")], default='')
        elif len(userlist)== 1:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'),("All","All"),(userlist[0].lower(), userlist[0])], default='')
        elif len(userlist)== 2:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'),("All","All"), (userlist[0].lower(), userlist[0]),(userlist[1].lower(),userlist[1])], default='')
        elif len(userlist)==3:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'),("All","All"), (userlist[0].lower(), userlist[0]),(userlist[1].lower(),userlist[1]),(userlist[2].lower(),userlist[2])], default='')
        elif len(userlist)==4:
            bank = SelectField('Bank', [validators.DataRequired()],choices=[('null', 'Select'),("All","All"),(userlist[0].lower(), userlist[0]),(userlist[1].lower(),userlist[1]),(userlist[2].lower(),userlist[2]),(userlist[3].lower(),userlist[3])], default='')
    form = newTransaction(request.form)
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
    elif month == 4:
        month = "Apr " + str(now.year)
    elif month == 5:
        month = "May " + str(now.year)
    prevvmonth = now.month-1
    if prevvmonth == 1:
        prevvmonth = "Jan"
    elif prevvmonth == 2:
        prevvmonth = "Feb"
    elif prevvmonth == 3:
        prevvmonth = "Mar"
    elif prevvmonth == 4:
        prevvmonth = "Apr"
    elif prevvmonth==5:
        prevvmonth="May"
    elif prevvmonth==6:
        prevvmonth="June"
    elif prevvmonth==7:
        prevvmonth="July"
    elif prevvmonth==8:
        prevvmonth="Aug"
    elif prevvmonth==9:
        prevvmonth="Sep"
    elif prevvmonth==10:
        prevvmonth="Oct"
    elif prevvmonth==11:
        prevvmonth="Nov"
    else:
        prevvmonth="Dec"

    justmonth = now.month
    if justmonth == 1:
        justmonth = "Jan"
    elif justmonth == 2:
        justmonth = "Feb"
    elif justmonth == 3:
        justmonth = "Mar"
    elif justmonth == 4:
        justmonth = "Apr"
    elif justmonth==5:
        justmonth="May"
    elif justmonth==6:
        justmonth="June"
    elif justmonth==7:
        justmonth="July"
    elif justmonth==8:
        justmonth="Aug"
    elif justmonth==9:
        justmonth="Sep"
    elif justmonth==10:
        justmonth="Oct"
    elif justmonth==11:
        justmonth="Nov"
    else:
        justmonth="Dec"

    if request.method == 'POST' and form.validate():
        hello=MainProcess.filter(session['userid'],form.bank.data,form.month.data)

    p = form.bank.data
    q = form.month.data
    if p=="":
        p="hi"
    if q=="":
        q="hi"
    hello = MainProcess.filter(session['userid'], form.bank.data, form.month.data)
    plist = MainProcess.spendinganalyticstransaction(session["userid"])
    totalprevdeposit = MainProcess.deposits(session["userid"], prevmonth)
    totalprevwithdraw = MainProcess.spendings(session["userid"], prevmonth)
    totaldeposit = MainProcess.deposits(session["userid"], month)
    totalwithdraw = MainProcess.spendings(session["userid"], month)
    totalforfilterdeposit=MainProcess.totalforfilterdeposit(session["userid"],form.month.data,form.bank.data)
    totalforfilterwithdraw=MainProcess.totalforfilterwithdraw(session['userid'],form.month.data,form.bank.data)
    return render_template("prevtransaction.html",totalforfilterwithdraw=totalforfilterwithdraw,totalforfilterdeposit=totalforfilterdeposit,prevvmonth=prevvmonth,justmonth=justmonth,another=plist,p=p,q=q,Transaction=hello,totalprevdeposit=totalprevdeposit,totalprevwithdraw=totalprevwithdraw,totaldeposit=totaldeposit,totalwithdraw=totalwithdraw,month=month,prevmonth=prevmonth,form=form)

class qtypoints(Form):

    choice1=SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1","Quantity:1"),("2","Quantity:2"),("3","Quantity:3")],default='')
    choice2=SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice3 = SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice4 = SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice5 = SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice6= SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice7= SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice8= SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice9= SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice10= SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice11= SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')
    choice12= SelectField('Quantity:', [validators.DataRequired()],choices=[('', 'Select'), ("1", "Quantity:1"), ("2", "Quantity:2"), ("3", "Quantity:3")],default='')

@app.route('/rewards',methods=['GET',"POST"])
def rewards():
    from datetime import datetime
    form = qtypoints(request.form)
    count = processpoint.processing(session['userid'])

    if form.choice11.data == '1':
        if count < 50:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-50")
            redeem = processpoint.redemption(session["userid"], "50", "Ben and Jerry")
    elif form.choice11.data == '2':
        if count < 100:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-100")
            redeem = processpoint.redemption(session["userid"], "100", "2x Ben and Jerry")
    elif form.choice11.data == '3':
        if count < 150:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-150")
            redeem = processpoint.redemption(session["userid"], "150", "3x Ben and Jerry")


    elif form.choice4.data == '1':
        if count < 100:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-100")
            redeem = processpoint.redemption(session["userid"], "100", "Polar")
    elif form.choice4.data == '2':
        if count < 200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-200")
            redeem = processpoint.redemption(session["userid"], "200", "2x Polar")
    elif form.choice4.data == '3':
        if count < 300:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-300")
            redeem = processpoint.redemption(session["userid"], "300", "3x Polar")


    elif form.choice6.data == '1':
        if count < 100:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-100")
            redeem = processpoint.redemption(session["userid"], "100", "Fairprice")
    elif form.choice6.data == '2':
        if count < 200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-200")
            redeem = processpoint.redemption(session["userid"], "200", "2x Fairprice")
    elif form.choice6.data == '3':
        if count < 300:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-300")
            redeem = processpoint.redemption(session["userid"], "300", "3x Fairprice")

    elif form.choice9.data == '1':
        if count < 100:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-100")
            redeem = processpoint.redemption(session["userid"], "100", "Swensen")
    elif form.choice9.data == '2':
        if count < 200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-200")
            redeem = processpoint.redemption(session["userid"], "200", "2x Swensen")
    elif form.choice9.data == '3':
        if count < 300:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-300")
            redeem = processpoint.redemption(session["userid"], "300", "3x Swensen")


    elif form.choice1.data == '1':
        if count < 200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-200")
            redeem = processpoint.redemption(session["userid"], "200", "Golden Village")
    elif form.choice1.data == '2':
        if count < 400:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-400")
            redeem = processpoint.redemption(session["userid"], "400", "2x Golden Village")
    elif form.choice1.data == '3':
        if count < 600:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-600")
            redeem = processpoint.redemption(session["userid"], "600", "3x Golden Village")

    elif form.choice2.data == '1':
        if count < 200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-200")
            redeem = processpoint.redemption(session["userid"], "200", "Restaurant")
    elif form.choice2.data == '2':
        if count < 400:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-400")
            redeem = processpoint.redemption(session["userid"], "400", "2x Restaurant")
    elif form.choice2.data == '3':
        if count < 600:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-600")
            redeem = processpoint.redemption(session["userid"], "600", "3x restaurant")

    elif form.choice5.data == '1':
        if count < 200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-200")
            redeem = processpoint.redemption(session["userid"], "200", "CrystalJade")
    elif form.choice5.data == '2':
        if count < 400:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-400")
            redeem = processpoint.redemption(session["userid"], "400", "2x CrystalJade")
    elif form.choice5.data == '3':
        if count < 600:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-600")
            redeem = processpoint.redemption(session["userid"], "600", "3x CrystalJade")

    elif form.choice8.data == '1':
        if count < 200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-200")
            redeem = processpoint.redemption(session["userid"], "200", "SakaeSushi")
    elif form.choice8.data == '2':
        if count < 400:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-400")
            redeem = processpoint.redemption(session["userid"], "400", "2x SakaeSushi")
    elif form.choice8.data == '3':
        if count < 600:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-600")
            redeem = processpoint.redemption(session["userid"], "600", "3x SakaeSushi")

    elif form.choice10.data == '1':
        if count < 200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-200")
            redeem = processpoint.redemption(session["userid"], "200", "Ikea")
    elif form.choice10.data == '2':
        if count < 400:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-400")
            redeem = processpoint.redemption(session["userid"], "400", "2x Ikea")
    elif form.choice10.data == '3':
        if count < 600:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-600")
            redeem = processpoint.redemption(session["userid"], "600", "3x Ikea")

    elif form.choice3.data == '1':
        if count < 300:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-300")
            redeem = processpoint.redemption(session["userid"], "300", "CapitalLand")
    elif form.choice3.data == '2':
        if count < 600:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-600")
            redeem = processpoint.redemption(session["userid"], "600", "2x CapitalLand")
    elif form.choice3.data == '3':
        if count < 900:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-900")
            redeem = processpoint.redemption(session["userid"], "900", "3x CapitalLand")


    elif form.choice7.data == '1':
        if count < 300:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-300")
            redeem = processpoint.redemption(session["userid"], "300", "Toyrus")
    elif form.choice7.data == '2':
        if count < 600:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-600")
            redeem = processpoint.redemption(session["userid"], "600", "2x Toyrus")
    elif form.choice7.data == '3':
        if count < 900:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-900")
            redeem = processpoint.redemption(session["userid"], "900", "3x Toyrus")

    elif form.choice12.data == '1':
        if count < 400:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-400")
            redeem = processpoint.redemption(session["userid"], "400", "Nex")
    elif form.choice12.data == '2':
        if count < 800:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-800")
            redeem = processpoint.redemption(session["userid"], "800", "2x Nex")
    elif form.choice12.data == '3':
        if count < 1200:
            tkinter.messagebox.showinfo('Alert!', 'Not enough points')
        else:
            count = processpoint.newpoint(session['userid'], "-1200")
            redeem = processpoint.redemption(session["userid"], "1200", "3x Nex")

    now = datetime.now()
    d1 = datetime(2018, 8, 31)
    d2 = datetime(2018, 8, 31)
    d3 = datetime(2018, 3, 31)
    d4 = datetime(2018, 7, 31)
    d5 = datetime(2018, 6, 30)
    d6 = datetime(2018, 6, 30)
    d7 = datetime(2018, 3, 31)
    d8 = datetime(2018, 12, 31)
    d9 = datetime(2018, 12, 31)
    d10 = datetime(2018, 5, 31)
    d11 = datetime(2018, 5, 31)
    d12 = datetime(2018, 2, 28)

    redeemed = processpoint.processpoint(session['userid'])
    count = processpoint.processing(session['userid'])
    pts = processpoint.calculate_point(session['userid'])
    newpt = open("point.txt", "a")
    newpt.write(session['userid'] + "," + str(pts) + "\n")

    return render_template('rewards.html', form=form, redeemed=redeemed, count=count, now=now, d1=d1, d2=d2, d3=d3,
                           d4=d4, d5=d5, d6=d6,
                           d7=d7, d8=d8, d9=d9, d10=d10, d11=d11, d12=d12)


@app.route('/logout')
def logout():
    session.pop("userid",None)
    flash("Logged Out Successfully")
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
