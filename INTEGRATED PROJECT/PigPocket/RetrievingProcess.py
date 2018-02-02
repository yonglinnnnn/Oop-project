import datetime
from BankAccounts import BankAccounts, FixedDeposit

months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def processUserDetails(name):
    detailsList = []
    try:
        user_file = open('file/'+name.capitalize(), 'r')
        for dlist in user_file:
            accountList = dlist.split(',')
            if accountList[2].lower() == "fixed deposit":
                s = FixedDeposit(accountList[0], accountList[1], accountList[2], accountList[3], accountList[4], accountList[5], accountList[6], accountList[7], accountList[8], accountList[9])
                StartDate = datetime.datetime.strptime(accountList[7], "%d-%m-%Y")
                newStartDate = str(StartDate.day) + " " + str(months[StartDate.month - 1]) + " " + str(StartDate.year)
                s.set_startDate(newStartDate)
                EndDate = datetime.datetime.strptime(accountList[8], "%d-%m-%Y")
                newEndDate = str(EndDate.day) + " " + str(months[EndDate.month - 1]) + " " + str(EndDate.year)
                s.set_endDate(newEndDate)
                detailsList.append(s)
            else:
                s = BankAccounts(accountList[0], accountList[1], accountList[2], accountList[3], accountList[4], accountList[5])
                detailsList.append(s)
        user_file.close()
        return detailsList
    except IOError:
        print("File not found")
        return detailsList
    except:
        print("Unknown error")
        return detailsList


def processBankBranches(name):
    branchesList = []
    try:
        branchesDetail = open('file/' + name.capitalize(), 'r')
        for branch in branchesDetail:
            list = branch.split(',')
            if list[0] not in branchesList:
                branchesList.append(list[0])
        branchesDetail.close()
        return branchesList
    except IOError:
        print("File not found")
        return branchesList
    except:
        print("Unknown error")
        return branchesList

def processBankType(name):
    typeList = []
    try:
        typeDetail = open('file/' + name.capitalize(), 'r')
        for type in typeDetail:
            list = type.split(',')
            if list[2] not in typeList:
                typeList.append(list[2])
        typeDetail.close()
        return typeList
    except IOError:
        print("File not found")
        return typeList
    except:
        print("Unknown error")
        return typeList

def processWithdrawal(accountNumber, month, year):
    total = 0
    try:
        t_file = open('file/' + str(accountNumber), 'r')
        for trans in t_file:
            list = trans.split(',')

            if list[5].lower() != "none":
                if list[6] == month and list[7] == (year + "\n"):
                    total += float(list[5])

        t_file.close()
        return total
    except IOError:
        print("File not found")
        return total
    except:
        print("Unknown error")
        return total


def processDeposit(accountNumber, month, year):
    total = 0
    try:
        t_file = open('file/' + str(accountNumber), 'r')
        for trans in t_file:
            list = trans.split(',')

            if list[4].lower() != "none":
                if list[6] == month and list[7] == (year + "\n"):
                    total += float(list[4])

        t_file.close()
        return total
    except IOError:
        print("File not found")
        return total
    except:
        print("Unknown error")
        return total
