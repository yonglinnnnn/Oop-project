from BankAccounts import BankAccounts

def processUserDetails(name):
    detailsList = []
    user_file = open('file/' + name.capitalize(), 'r')
    for dlist in user_file:
        list = dlist.split(',')
        s = BankAccounts(list[0], list[1], list[2], float(list[3]), float(list[4]), float(list[5]))

        detailsList.append(s)
    return detailsList