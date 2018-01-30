from Transaction import Transaction
import datetime


def ProcessTransaction(name):
    userlist=[]
    user_file=open("file/Transaction.txt",'r')
    for ulist in user_file:
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
    spending=name+","+month+","+"Withdraw"+","+withdraw+"\n"
    user=open("file/SpendingAnalytics.txt","a")
    user_file=open("file/Transaction.txt","a")
    if bank_details.endswith("010-4-444444"):
        detailsList = []
        user_file = open('file/' + name.capitalize(), 'r')
        for dlist in user_file:
            list = dlist.split(',')
            if bank_details.endswith(list[1]):
                s = float(list[5])
                detailsList.append(s)
        acc=open("file/010-4-444444","a")
        accs=open("file/" + name,"w")
        total= detailsList[0]-float(withdraw)
        total="%0.2f"%total
        u="DBS,010-4-444444,savings,0.1,700.0," + str(total) +"\n"
        i="DBS,010-1-111111,current,0.0,2500.0,2500.0"+"\n"
        o="OCBC,550-10-89550,savings,0.4,1000.0,1500.0"+"\n"
        accs.write(u)
        accs.write(i)
        accs.write(o)
        p="Withdraw" + "," + "$" + "," + withdraw + "\n"
        acc.write(p)
        userdata = name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
        spending = name + "," + month + "," + "Withdraw" + "," + withdraw + "\n"
        user = open("file/SpendingAnalytics.txt", "a")
        user_file = open("file/Transaction.txt", "a")
    elif bank_details.endswith("010-1-111111"):
        detailsList = []
        user_file = open('file/' + name.capitalize(), 'r')
        for dlist in user_file:
            list = dlist.split(',')
            if bank_details.endswith(list[1]):
                s = float(list[5])
                detailsList.append(s)
        acc = open("file/010-1-111111", "a")
        accs = open("file/" + name, "w")
        total = detailsList[0] - float(withdraw)
        total = "%0.2f" % total
        u = "DBS,010-4-444444,savings,0.1,700.0,600.0" + "\n"
        i = "DBS,010-1-111111,current,0.0,2500.0," + str(total)+ "\n"
        o = "OCBC,550-10-89550,savings,0.4,1000.0,1500.0" + "\n"
        accs.write(u)
        accs.write(i)
        accs.write(o)
        p = "Withdraw" + "," + "$" + "," + withdraw + "\n"
        acc.write(p)
        userdata = name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
        spending = name + "," + month + "," + "Withdraw" + "," + withdraw + "\n"
        user = open("file/SpendingAnalytics.txt", "a")
        user_file = open("file/Transaction.txt", "a")


    user_file.write(userdata)
    user.write(spending)

def CurrentTransaction(name, month, type):
    t_file = open('file/SpendingAnalytics.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')
        if list[0] == name and list[1] == month and list[2] == type:
            total += float(list[3])
    return float("{0:.2f}".format(total))

def Totalamount(name,type):
    t_file = open('file/SpendingAnalytics.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')
        if list[0] == name and list[2] == type:
            total += float(list[3])
    return float("{0:.2f}".format(total))



