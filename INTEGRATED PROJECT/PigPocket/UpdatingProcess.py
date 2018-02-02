import datetime
from datetime import timedelta
import RetrievingProcess
from BankAccounts import FixedDeposit, BankAccounts

# accountList[4] is the principal amount for fixed deposit or original amount for non-fixed deposit
# accountList[5] is the matured amount for fixed deposit or account Balance for non-fixed deposit
# accountList[7] is the start date for fixed deposit
# accountList[8] is the end date for fixed deposit

months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def updateaccountDetails(name):
    AccountList = []
    fixedDepositList = []
    account_file = open("file/"+name.capitalize(), 'r')
    for account in account_file:
        accountList = account.split(',')
        if accountList[2].lower() == "fixed deposit":
            s = FixedDeposit(accountList[0],accountList[1],accountList[2],accountList[3],accountList[4],accountList[5],accountList[6],accountList[7],accountList[8],accountList[9])
            StartDate = datetime.datetime.strptime(accountList[7], "%d-%m-%Y")
            EndDate = datetime.datetime.strptime(accountList[8], "%d-%m-%Y")
            currDate = datetime.datetime.strptime(str(datetime.datetime.now().date()), "%Y-%m-%d").strftime('%d-%m-%Y')
            currDate = datetime.datetime.strptime(str(currDate),"%d-%m-%Y")
            totalDay = int(accountList[6]) * 365
            accountDetails =""
            if currDate == EndDate:
                accountList[9] = "Y"
                newBalance = float(accountList[4]) + (((float(accountList[3]) / 100) * float(accountList[4])) * 3)
                s.set_accountBal(newBalance)
                accountDetails = accountList[0] + ',' + accountList[1] + ',' + accountList[2] + ',' + accountList[3] + ',' + accountList[4] + ',' + str(newBalance) + ',' + accountList[6] + ',' + (str(StartDate.day) + '-' + str(StartDate.month) + '-' + str(StartDate.year) + ',' + (str(EndDate.day) + '-' + str(EndDate.month) + '-' + str(EndDate.year)) + ',' + accountList[9] + ',' + '\n')
            elif currDate > EndDate:
                accountList[9] = "N"
                dayDifference = currDate - EndDate
                dayDifference = str(dayDifference).split()
                StartDate = datetime.datetime.strptime(accountList[8], "%d-%m-%Y")
                totalDay = (int(accountList[6]) * 365)
                EndDate = datetime.datetime.strptime(accountList[8], "%d-%m-%Y") + timedelta(days=totalDay)
                EndDate = datetime.datetime.strptime(str(EndDate.date()), "%Y-%m-%d").strftime('%d-%m-%Y')
                EndDate = datetime.datetime.strptime(str(EndDate), "%d-%m-%Y")

                s.set_originalaccountBal(accountList[5])

                dayDifference = int(dayDifference[0]) // 365
                newBalance = float(accountList[4]) + (
                (float(accountList[3]) / 100) * float(accountList[4]) * (int(accountList[6]) - dayDifference))
                s.set_accountBal(newBalance)
                s.set_originalaccountBal(s.get_accountBal())
                accountDetails = accountList[0] + ',' + accountList[1] + ',' + accountList[2] + ',' + accountList[3] + ',' + str(s.get_originalaccountBal()) + ',' + str(s.get_accountBal()) + ',' + accountList[6] + ',' + (str(StartDate.day) + '-' + str(StartDate.month) + '-' + str(StartDate.year) + ',' + (str(EndDate.day) + '-' + str(EndDate.month) + '-' + str(EndDate.year)) + ',' +accountList[9] + ',' + '\n')
            else:
                accountList[9] = "N"
                dayDifference = EndDate - currDate
                dayDifference = str(dayDifference).split()
                dayDifference = int(dayDifference[0]) // 365
                newBalance = float(accountList[4]) + ((float(accountList[3])/100) * float(accountList[4]) * (int(accountList[6]) - dayDifference))
                s.set_accountBal(newBalance)
                accountDetails = accountList[0] + ',' + accountList[1] + ',' + accountList[2] + ',' + accountList[3] + ',' + accountList[4] + ',' + str(s.get_accountBal()) + ',' + accountList[6] + ',' + (str(StartDate.day)+'-'+str(StartDate.month)+'-'+str(StartDate.year) + ',' + (str(EndDate.day)+'-'+str(EndDate.month)+'-'+str(EndDate.year)) + ',' + accountList[9] + ',' + '\n')

            AccountList.append(accountDetails)
            fixedDepositList.append(s)
        else:
            s = BankAccounts(accountList[0], accountList[1], accountList[2], accountList[3], accountList[4], accountList[5])
            accountDetails = accountList[0] + ',' + accountList[1] + ',' + accountList[2] + ',' + accountList[3] + ',' + accountList[4] + ',' + accountList[5]
            AccountList.append(accountDetails)
    account_file.close()
    account_file = open("file/"+name.capitalize(), 'w')
    for item in AccountList:
        account_file.write(item)
    account_file.close()
    return fixedDepositList

y = datetime.datetime.strptime("28-1-2018", "%d-%m-%Y")
x = datetime.datetime.strptime("28-2-2018", "%d-%m-%Y")
c = x + timedelta(days=365)
print(c)

