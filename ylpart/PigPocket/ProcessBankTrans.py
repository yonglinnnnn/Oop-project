from Transaction import Transaction

def process_accountTransaction(bankNo, monthNow, yearNow):
    transactions = []
    try:
        bankTransFile = open("file/" + bankNo, "r")
        for bankTrans in bankTransFile:
            list = bankTrans.split(',')
            s = Transaction(list[0], list[1], list[2], list[3], list[4], list[5])
            if list[6] == monthNow and list[7] == (yearNow + "\n"):
                transactions.append(s)
        bankTransFile.close()
        return transactions
    except IOError:
        print("File not found")
        return transactions
    except:
        print("Unknown error")
        return transactions
