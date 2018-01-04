from Transaction import Transaction

def processTransaction():
    userlist=[]
    user_file=open("Transaction.txt",'r')
    for ulist in user_file:
        list=ulist.split(',')
        s=Transaction(list[0],list[1],list[2],list[3],list[4],list[5])
        userlist.append(s)
    return userlist

def newTransaction(name,date,bank_details,transaction_details,deposit,withdraw):
    userdata=name + "," + date + "," + bank_details + "," + transaction_details + "," + deposit + "," + withdraw + "\n"
    user_file=open("Transaction.txt","a")
    user_file.write(userdata)



