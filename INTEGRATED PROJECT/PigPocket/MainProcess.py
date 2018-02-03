from Transaction import Transaction
from newgiro import NewGiroUser
from Users import Users
from Accounts import Accounts
from dateutil import relativedelta

import datetime
from datetime import date
from PigPocket.girodetails import showGiroDetails
today = date.today()
currentMonth = today.month

def newGiro(name,bankno, amount, payto, specify, date, category, month):
    userdata=(name + "," + bankno + "," + amount + "," + payto + "," + specify + "," + date + "," + category + "," + month)
    u_file = open('file/' + name , 'r')
    for amt in u_file:
        list = amt.split(',')
        if list[1] == bankno:
            print(list)
            if float(list[5]) > float((amount + "\n")):
                print(amount)
                userdetails = (name + ',' + amount + ',' + bankno + "," + date + "," + specify + "," + "Y" + "," + month )
                file = open('file/girotransactions.txt', 'a')
                file.write(userdetails + '\n')
            print(list[5])
            print(amount)
            if float(list[5]) < float((amount + "\n")):
                userdetails1 = (name + ',' + amount + ',' + bankno + "," + date + "," + specify + "," + "N" + "," + month)
                file = open('file/girotransactions.txt', 'a')
                file.write(userdetails1 + '\n')
        else:
            print('break')

    user_file=open('file/girodetails.txt', 'a')
    user_file.write(userdata + '\n')



def addUser(name):
    usersList = []

    user_file = open('file/girodetails.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == name:
            file = open('file/girotransactions.txt', 'r')
            for i in file:
                count = 0
                list1 = i.split(',')
                if list1[5] == 'Y':
                    count = count+1
                    months = int(currentMonth) - (int(list[7])-1)
                    total = months * int(list[2])
            s = NewGiroUser(list[0], list[1], list[2], list[3], list[4], list[5], list[6], total, currentMonth)

            usersList.append(s)
    return usersList



def displaydetails(bankno, specify):
    lList=[]
    file = open('file/girotransactions.txt', 'r')
    for flist in file:
        list = flist.split(',')
        monthsdiff = int(currentMonth) - (int(list[6]) - 1)
        if list[2]==bankno and list[4]==specify:


            if list[5] == 'Y':
                s = showGiroDetails(list[0], list[1], list[2], list[3] , list[4], "Yes" , monthsdiff)
                lList.append(s)
            elif list[5] == "N":
                s = showGiroDetails(list[0], list[1], list[2], list[3], list[4], "No", monthsdiff)
                lList.append(s)

    return lList



def ProcessTransaction(name):
    userlist=[]
    user_file=open("file/Transaction.txt",'r')
    for ulist in reversed(user_file.readlines()):
            list=ulist.split(',')
            if list[0]== name:
                s=Transaction(list[0],list[1],list[2],list[3],list[4],list[5])
                userlist.append(s)
    return userlist


def newTransaction(name,date,bank_details,transaction_details,deposit,withdraw):
    userdata=name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
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
    justmonth=now.month
    if justmonth==1:
        justmonth="Jan"
    elif justmonth==2:
        justmonth="Feb"
    elif justmonth==3:
        justmonth="Mar"
    elif justmonth==3:
        justmonth="Apr"
    Alltrans = userdata = name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "," + justmonth + "," + str(now.year) + "," + "\n"
    spending=name+","+month+","+"Withdraw"+","+withdraw+"\n"
    user=open("file/SpendingAnalytics.txt","a")
    user_file=open("file/Transaction.txt","a")
    All=open("file/AllTransaction.txt","a")
    if bank_details.endswith("010-4-444444"):
        detailsList = []
        others=[]
        user_file = open('file/' + name.capitalize(), 'r')
        for dlist in user_file:
            list = dlist.split(',')
            if bank_details.endswith(list[1]):
                s = float(list[5])
                detailsList.append(s)
            else:
                q=float(list[5])
                others.append(q)
        acc=open("file/010-4-444444","a")
        accs=open("file/" + name,"w")
        total= detailsList[0]-float(withdraw)
        total="%0.2f"%total
        print(total)
        u="DBS,010-4-444444,savings,0.1,700.00," + str(total) + "\n"
        i="DBS,010-1-111111,current,0.0,2500.00,"+ str(others[0]) + "\n"
        o="OCBC,550-10-89550,savings,0.4,1000.00,"+ str(others[1]) + "\n"
        accs.write(u)
        accs.write(i)
        accs.write(o)
        p=name + "," + date + "," + bank_details + "," + transaction_details +"," + "None," + withdraw  + "," + justmonth + "," + str(now.year) + "," + "\n"
        acc.write(p)
        userdata = name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
        spending = name + "," + month + "," + "Withdraw" + "," + withdraw + "\n"
        user = open("file/SpendingAnalytics.txt", "a")
        user_file = open("file/Transaction.txt", "a")
        All = open("file/AllTransaction.txt", "a")

    elif bank_details.endswith("010-1-111111"):
        detailsList = []
        others=[]
        user_file = open('file/' + name.capitalize(), 'r')
        for dlist in user_file:
            list = dlist.split(',')
            if bank_details.endswith(list[1]):
                s = float(list[5])
                detailsList.append(s)
            else:
                q=float(list[5])
                others.append(q)
        acc=open("file/010-1-111111","a")
        accs=open("file/" + name,"w")
        total= detailsList[0]-float(withdraw)
        total="%0.2f"%total
        u="DBS,010-4-444444,savings,0.1,700.00," + str(others[0]) +"\n"
        i="DBS,010-1-111111,current,0.0,2500.00,"+ str(total) + "\n"
        o="OCBC,550-10-89550,savings,0.4,1000.00,"+ str(others[1]) + "\n"
        accs.write(u)
        accs.write(i)
        accs.write(o)
        p=name + "," + date + "," + bank_details + "," + transaction_details +"," + "None," + withdraw  + "," + justmonth + "," + str(now.year) + "," + "\n"
        acc.write(p)
        userdata = name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
        spending = name + "," + month + "," + "Withdraw" + "," + withdraw + "\n"
        user = open("file/SpendingAnalytics.txt", "a")
        user_file = open("file/Transaction.txt", "a")
        All = open("file/AllTransaction.txt", "a")
    elif bank_details.endswith("550-10-89550"):
        detailsList = []
        others=[]
        user_file = open('file/' + name.capitalize(), 'r')
        for dlist in user_file:
            list = dlist.split(',')
            if bank_details.endswith(list[1]):
                s = float(list[5])
                detailsList.append(s)
            else:
                q=float(list[5])
                others.append(q)
        acc=open("file/550-10-89550","a")
        accs=open("file/" + name,"w")
        total= detailsList[0]-float(withdraw)
        total="%0.2f"%total
        u="DBS,010-4-444444,savings,0.1,700.00," + str(others[0]) +"\n"
        i="DBS,010-1-111111,current,0.0,2500.00,"+ str(others[1]) + "\n"
        o="OCBC,550-10-89550,savings,0.4,1000.00,"+ str(total) + "\n"
        accs.write(u)
        accs.write(i)
        accs.write(o)
        p=name + "," + date + "," + bank_details + "," + transaction_details +"," + "None," + withdraw  + "," + justmonth + "," + str(now.year) + "\n"
        acc.write(p)
        userdata = name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
        spending = name + "," + month + "," + "Withdraw" + "," + withdraw + "\n"
        user = open("file/SpendingAnalytics.txt", "a")
        user_file = open("file/Transaction.txt", "a")
        All = open("file/AllTransaction.txt", "a")
    else:
        detailsList = []
        others=[]
        user_file = open('file/' + name.capitalize(), 'r')
        for dlist in user_file:
            list = dlist.split(',')
            if bank_details.endswith(list[1]):
                s = float(list[5])
                detailsList.append(s)
            else:
                q=float(list[5])
                others.append(q)
        acc=open("file/910-20-31012","a")
        accs=open("file/" + name,"w")
        total= detailsList[0]-float(withdraw)
        total="%0.2f"%total
        o="UOB,910-20-31012,hybrid(savings+current),0.5,5000.00,"+ str(total) + "\n"
        c="UOB,911-21-31013,fixed deposit,1.2,30000.00,30360.00,3,28-1-2018,28-1-2021,N,\n"
        u="OCBC,550-10-89551,fixed deposit,1.1,40000.00,40000.00,4,1-2-2018,1-2-2022,N,\n"
        accs.write(o)
        accs.write(c)
        accs.write(u)
        p=name + "," + date + "," + bank_details + "," + transaction_details +"," + "None," + withdraw  + "," + justmonth + "," + str(now.year) + "\n"
        acc.write(p)
        userdata = name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
        spending = name + "," + month + "," + "Withdraw" + "," + withdraw + "\n"
        user = open("file/SpendingAnalytics.txt", "a")
        user_file = open("file/Transaction.txt", "a")
        All = open("file/AllTransaction.txt", "a")


    All.write(Alltrans)
    user_file.write(userdata)
    user.write(spending)

def CurrentTransaction(name, month, type):
    t_file = open('file/SpendingAnalytics.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')
        if list[0] == name and list[1] == month and list[2] == type:
            total += float(list[3])
    s="%0.2f"%total
    return s

def Totalamount(name,type):
    t_file = open('file/SpendingAnalytics.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')
        if list[0] == name and list[2] == type:
            total += float(list[3])
    s = "%0.2f" % total
    return s


def spendings(name,month):
    t_file=open("file/010-1-111111","r")
    total=0
    for i in t_file:
        list=i.split(",")
        if list[0]==name and list[1].endswith(month) and list[4]=="None":
            total+=float(list[5])
    n_file=open("file/010-4-444444","r")
    for u in n_file:
        list=u.split(",")
        if list[0]==name and list[1].endswith(month) and list[4]=="None":
            total+=float(list[5])
    m_file=open("file/550-10-89550","r")
    for m in m_file:
        list=m.split(",")
        if list[0]==name and list[1].endswith(month) and list[4]=="None":
            total+=float(list[5])
    kel_file=open("file/910-20-31012","r")
    for k in kel_file:
        list=k.split(",")
        if list[0]==name and list[1].endswith(month) and list[4]=="None":
            total+=float(list[5])
    s = "%0.2f" % total
    return s

def deposits(name,month):
    t_file=open("file/010-4-444444","r")
    total=0
    for i in t_file:
        list=i.split(",")
        if list[0]==name and list[1].endswith(month) and list[5]=="None":
            total+=float(list[4])
    u_file = open("file/010-1-111111", "r")
    for i in u_file:
        list = i.split(",")
        if list[0] == name and list[1].endswith(month) and list[5] == "None":
            total += float(list[4])
    k_file = open("file/550-10-89550", "r")
    for i in k_file:
        list = i.split(",")
        if list[0] == name and list[1].endswith(month) and list[5] == "None":
            total += float(list[4])
    kel_file = open("file/910-20-31012", "r")
    for i in kel_file:
        list = i.split(",")
        if list[0] == name and list[1].endswith(month) and list[5] == "None":
            total += float(list[4])
    s = "%0.2f"%total
    return s
"""
def spendinganalyticstransaction(name):
    userlist = []
    user_file = open("file/010-1-111111", 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == name:
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)
    use_file = open("file/010-4-444444", 'r')
    for llist in use_file:
        list = llist.split(',')
        if list[0] == name:
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)
    r_file = open("file/550-10-89550", 'r')
    for plist in r_file:
        list = plist.split(',')
        if list[0] == name:
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)
    users_file = open("file/910-20-31012", 'r')
    for nlist in users_file:
        list = nlist.split(',')
        if list[0] == name:
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)

    return userlist
    """
def spendinganalyticstransaction(name):
    userlist = []
    user_file = open("file/Alltransaction.txt", 'r')
    for ulist in reversed(user_file.readlines()):
        list = ulist.split(',')
        if list[0] == name:
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)
    return userlist

"""
def filter(name,bank,date):
    userlist = []
    user_file = open("file/010-1-111111", 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == name and list[6]==date:
            if list[2].startswith(bank.capitalize()) or list[2].startswith(bank.upper()):
                s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
                userlist.append(s)
        elif list[0] == name and list[6]==date and bank=="All":
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)

    use_file = open("file/010-4-444444", 'r')
    for llist in use_file:
        list = llist.split(',')
        if list[0] == name and list[6]==date:
            if list[2].startswith(bank.capitalize()) or list[2].startswith(bank.upper()):
                s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
                userlist.append(s)
        elif list[0] == name and list[6]==date and bank=="All":
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)

    r_file = open("file/550-10-89550", 'r')
    for plist in r_file:
        list = plist.split(',')
        if list[0] == name and list[6]==date:
            if list[2].startswith(bank.capitalize()) or list[2].startswith(bank.upper()):
                s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
                userlist.append(s)
        elif list[0] == name and list[6]==date and bank=="All":
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)

    users_file = open("file/910-20-31012", 'r')
    for nlist in users_file:
        list = nlist.split(',')
        if list[0] == name and list[6]==date:
            if list[2].startswith(bank.capitalize()) or list[2].startswith(bank.upper()):
                s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
                userlist.append(s)
        elif list[0] == name and list[6]==date and bank=="All":
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)

    return userlist
"""
def filter(name,bank,date):
    userlist = []
    user_file = open("file/AllTransaction.txt", 'r')
    for ulist in reversed(user_file.readlines()):
        list = ulist.split(',')
        if list[0] == name and list[6]==date and bank=="All":
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            userlist.append(s)
        elif list[0] == name and list[6]==date:
            if list[2].startswith(bank.capitalize()) or list[2].startswith(bank.upper()):
                s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
                userlist.append(s)

    return userlist

def loginUser():

    userList = []
    user_info = open("file/users.txt", "r")
    for i in user_info:
        info = i.split(",")
        u = Users(info[0],info[1],info[2])
        userList.append(u)

    return userList

def savings(firstname, month, type):

    total = 0

    file1 = open('file/010-4-444444', 'r')
    for trans in file1:
        list = trans.split(',')
        if list[0] == firstname and list[4] == "None" and list[1].endswith(month):
            total -= float(list[5])
        elif list[0] == firstname and list[5] == "None" and list[1].endswith(month):
            total += float(list[4])

        file2 = open('file/550-10-89550', 'r')
        for trans in file2:
            list = trans.split(',')
            if list[0] == firstname and list[4] == "None" and list[1].endswith(month):
                total -= float(list[5])
            elif list[0] == firstname and list[5] == "None" and list[1].endswith(month):
                total += float(list[4])

        file4 = open('file/910-20-31012', 'r')
        for trans in file4:
            list = trans.split(',')
            if list[0] == firstname and list[4] == "None" and list[1].endswith(month):
                total -= float(list[5])
            elif list[0] == firstname and list[5] == "None" and list[1].endswith(month):
                total += float(list[4])

    total = "%.2f"%total
    return total


def current(firstname, month, type):

    total = 0

    file3 = open('file/010-1-111111', 'r')
    for trans in file3:
        list = trans.split(',')
        if list[0] == firstname and list[4] == "None" and list[1].endswith(month):
            total -= float(list[5])
        elif list[0] == firstname and list[5] == "None" and list[1].endswith(month):
            total += float(list[4])

    total = "%.2f"%total
    return total


def processFixedDeposit(firstname, nature):

    f_file = open('file/fixeddeposit.txt','r')
    total = 0
    for trans in f_file:
        list = trans.split(',')
        if list[0] == firstname and list[3] == nature:
            total += float(list[5])
    total = "%.2f" %total
    return total


def get_status_day(name):

    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    date=datetime.datetime(year,month,day)
    diff_day=0



    data_file = open("file/fixeddeposit.txt","r")
    for acc in data_file:
        data = acc.split(',')
        if data[0] == name:
            expiry = datetime.datetime(int(data[8]),int(data[7]),int(data[6]))
            diff = relativedelta.relativedelta(expiry, date)
            diff_day = diff.days

    return diff_day


def get_status_month(name):

    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    date=datetime.datetime(year,month,day)
    diff_month=0



    data_file = open("file/fixeddeposit.txt","r")
    for acc in data_file:
        data = acc.split(',')
        if data[0] == name:
            expiry = datetime.datetime(int(data[8]),int(data[7]),int(data[6]))
            diff = relativedelta.relativedelta(expiry, date)
            diff_month = diff.months

    return diff_month


def get_status_year(name):

    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    date=datetime.datetime(year,month,day)
    diff_year=0



    data_file = open("file/fixeddeposit.txt","r")
    for acc in data_file:
        data = acc.split(',')
        if data[0] == name:
            expiry = datetime.datetime(int(data[8]),int(data[7]),int(data[6]))
            diff = relativedelta.relativedelta(expiry, date)
            diff_year = diff.years

    return diff_year


def get_fd(name):
    count = 0
    fd = open("file/accounts.txt","r")
    for acc in fd:
        data = acc.split(',')
        if data[0] == name:
            if data[3] == 'fixed deposit':
                count += 1
    return count


def fd_table(name):
    fdList = []
    fd_info = open("file/fixeddeposit.txt", "r")
    for i in fd_info:
        info = i.split(",")
        if info[0] == name:
            a = Accounts(info[1], info[2], info[3])
            fdList.append(a)

    return fdList


def get_points(name):
    points = 0
    points_file = open("file/point.txt","r")
    for p in points_file:
        pts = p.split(",")
        if pts[0] == name:
            points += int(pts[1])
    return points

def s_balance(firstname,type):
    total = 0

    file = open("file/accounts.txt","r")
    for a in file:
        user = a.split(",")
        if user[0] == firstname and user[3] == type:
            total += float(user[5])

    file1 = open('file/010-4-444444', 'r')
    for trans in file1:
        list = trans.split(',')
        if list[0] == firstname and list[4] == "None" :
            total -= float(list[5])
        elif list[0] == firstname and list[5] == "None" :
            total += float(list[4])

        file2 = open('file/550-10-89550', 'r')
        for trans in file2:
            list = trans.split(',')
            if list[0] == firstname and list[4] == "None" :
                total -= float(list[5])
            elif list[0] == firstname and list[5] == "None" :
                total += float(list[4])

        file4 = open('file/910-20-31012', 'r')
        for trans in file4:
            list = trans.split(',')
            if list[0] == firstname and list[4] == "None" :
                total -= float(list[5])
            elif list[0] == firstname and list[5] == "None" :
                total += float(list[4])

    total = "%.2f" % total
    return total


def c_balance(firstname,type):
    total = 0

    file = open("file/accounts.txt", "r")
    for a in file:
        user = a.split(",")
        if user[0] == firstname and user[3] == type:
            total += float(user[5])

    file3 = open('file/010-1-111111', 'r')
    for trans in file3:
        list = trans.split(',')
        if list[0] == firstname and list[4] == "None" :
            total -= float(list[5])
        elif list[0] == firstname and list[5] == "None" :
            total += float(list[4])

    total = "%.2f" % total
    return total
