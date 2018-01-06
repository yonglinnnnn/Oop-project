from Transaction import Transaction

def processTransaction(name):
    userlist=[]
    user_file=open("Transaction.txt",'r')
    for ulist in user_file:
            list=ulist.split(',')
            if list[0]== name:
                s=Transaction(list[0],list[1],list[2],list[3],list[4],list[5])
                userlist.append(s)
    return userlist


def newTransaction(name,date,bank_details,transaction_details,deposit,withdraw):
    userdata=name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
    spending=name+","+"Jan"+","+"Withdraw"+","+withdraw+"\n"
    user=open("SpendingAnalytics.txt","a")
    user_file=open("Transaction.txt","a")
    user_file.write(userdata)
    user.write(spending)

def CurrentTransaction(name, month, type):
    t_file = open('SpendingAnalytics.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')
        if list[0] == name and list[1] == month and list[2] == type:
            total += float(list[3])
    return total

