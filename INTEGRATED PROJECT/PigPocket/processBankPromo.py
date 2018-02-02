from BankAccountPromotions import BankAccountPromotions
import datetime

months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def processBankPromo(bankBranch, accountType, currDate):
    bankPromos = []
    bankPromoFile = open('file/BankAccountPromotions', 'r')
    for bankPromo in bankPromoFile:
        list = bankPromo.split(',')
        s = BankAccountPromotions(list[0],list[1],list[2],list[3],list[4],list[5],list[6])
        if list[0] == bankBranch.lower() and list[1] == accountType.lower():
            if currDate == '':
                promoStartDate = datetime.datetime.strptime(str(list[2]), "%d-%m-%Y")
                promoEndDate = datetime.datetime.strptime(str(list[3]), "%d-%m-%Y")
                print('promo start date: {} and promo end date: {}.'.format(promoStartDate, promoEndDate))
            elif list[2] == '':
                newcurrDate = datetime.datetime.strptime(currDate, "%d-%m-%Y")
                promoEndDate = datetime.datetime.strptime(str(list[3]), "%d-%m-%Y")
                if newcurrDate <= promoEndDate:
                    promoEndDate = str(promoEndDate.day) + " " + months[promoEndDate.month - 1] + " " + str(promoEndDate.year)
                    s.set_endDate(promoEndDate)
                    bankPromos.append(s)
            elif list[3] == '':
                newcurrDate = datetime.datetime.strptime(currDate, "%d-%m-%Y")
                promoStartDate = datetime.datetime.strptime(str(list[2]), "%d-%m-%Y")
                if newcurrDate >= promoStartDate:
                    promoStartDate = str(promoStartDate.day) + " " + months[promoStartDate.month - 1] + " " + str(promoStartDate.year)
                    s.set_startDate(promoStartDate)
                    bankPromos.append(s)
            else:
                newcurrDate = datetime.datetime.strptime(currDate, "%d-%m-%Y")
                promoStartDate = datetime.datetime.strptime(str(list[2]), "%d-%m-%Y")
                promoEndDate = datetime.datetime.strptime(str(list[3]), "%d-%m-%Y")
                if newcurrDate >= promoStartDate and newcurrDate <= promoEndDate:
                    promoStartDate = str(promoStartDate.day) + " " + months[promoStartDate.month - 1] + " " + str(promoStartDate.year)
                    s.set_startDate(promoStartDate)
                    promoEndDate = str(promoEndDate.day) + " " + months[promoEndDate.month - 1] + " " + str(promoEndDate.year)
                    s.set_endDate(promoEndDate)
                    bankPromos.append(s)

    bankPromoFile.close()
    return bankPromos

y = datetime.datetime.strptime("28-1-2018", "%d-%m-%Y")
x = datetime.datetime.strptime("28-2-2018", "%d-%m-%Y")
c = x - y
c = str(c).split()
if int(c[0]) == 31:
    print(c[0])

