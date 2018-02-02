from point import point
from datetime import datetime

def processpoint(name):
    userlist = []
    user_file = open('file/redeem.txt', 'r')
    for i in user_file:
        list = i.split(',')
        if list[0] == name:
            s = point(list[0], list[1], list[2], list[3])
            userlist.append(s)
    return userlist


def countpoint():
    c_file = open('file/point.txt', 'a')
    total = 0


def processing(name):
    t_file = open('file/point.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')
        if list[0] == name:
            total += float(list[1])
    return total


def newpoint(name, point):
    userdata = name + ',' + point + "\n"
    user = open('file/point.txt', 'a')
    user.write(userdata)


def redemption(name, point, reward):
    today = datetime.now()
    now = str(today.date())
    user = name + "," + point + "," + reward + "," + now + "\n"
    file = open("file/redeem.txt", "a")
    file.write(user)


def calculate_point(name):
    total = 0
    save1 = 0
    # save2=0
    # save3=0
    save4 = 0
    pointfile = []
    pts = 0
    pts1 = 0
    pts2 = 0

    steven = open('file/Steven', 'r')
    Kelly = open('file/Kelly', 'r')
    s_file1 = open('file/010-1-111111', 'r')
    s_file2 = open('file/010-4-444444', 'r')
    s_file3 = open('file/550-10-89550', 'r')
    k_file1 = open('file/910-20-31012', 'r')

    for i in s_file1:
        list = i.split(",")
        if list[0] == name:
            if list[4] == 'None':
                deposit = 0
                save1 = deposit - float(list[5])
                # total1 += save1
                if save1 < 200:
                    pts += 0
                elif save1 >= 200 and save1 < 1000:
                    pts += (save1 / 10) * 2
                else:
                    pts += (save1 / 10) * 4

            elif list[5] == 'None':
                withdraw = 0
                save1 = float(list[4]) - withdraw
                # total1+=save1
                if save1 < 200:
                    pts += 0
                elif save1 >= 200 and save1 < 1000:
                    pts += (save1 / 10) * 2
                else:
                    pts += (save1 / 10) * 4

            else:
                pts += 0

    for i in s_file2:
        list = i.split(",")
        if list[0] == name:
            if list[4] == 'None':
                deposit = 0
                save2 = deposit - float(list[5])
                # total2 += save2
                if save2 < 200:
                    pts += 0
                elif save2 >= 200 and save2 < 1000:
                    pts += (save2 / 10) * 2
                else:
                    pts += (save2 / 10) * 4

            elif list[5] == 'None':
                withdraw = 0
                save2 = float(list[4]) - withdraw
                # total2 += save2
                if save2 < 200:
                    pts += 0
                elif save2 >= 200 and save2 < 1000:
                    pts += (save2 / 10) * 2
                else:
                    pts += (save2 / 10) * 4

            else:
                pts += 0

    for i in s_file3:
        list = i.split(",")
        if list[0] == name:
            if list[4] == 'None':
                deposit = 0
                save3 = deposit - float(list[5])
                # total3 += save3
                if save3 < 200:
                    pts += 0
                elif save3 >= 200 and save3 < 1000:
                    pts += (save3 / 10) * 2
                else:
                    pts += (save3 / 10) * 4

            elif list[5] == 'None':
                withdraw = 0
                save3 = float(list[4]) - withdraw
                # total3 += save3
                if save3 < 200:
                    pts += 0
                elif save3 >= 200 and save3 < 1000:
                    pts += (save3 / 10) * 2
                else:
                    pts += (save3 / 10) * 4

            else:
                pts += 0

    for i in k_file1:
        list = i.split(",")
        if list[0] == name:
            if list[4] == 'None':
                deposit = 0
                save4 = deposit - float(list[5])
                # total4 += save4
                if save4 < 200:
                    pts += 0
                elif save4 >= 200 and save4 < 1000:
                    pts += (save4 / 10) * 2
                else:
                    pts += (save4 / 10) * 4

            elif list[5] == 'None':
                withdraw = 0
                save4 = float(list[4]) - withdraw
                # total4 += save4
                if save4 < 200:
                    pts += 0
                elif save4 >= 200 and save4 < 1000:
                    pts += (save4 / 10) * 2
                else:
                    pts += (save4 / 10) * 4

            else:
                pts += 0

    pts = "%d" % pts
    return pts


a = calculate_point("Steven")
print(a)
b = calculate_point("Kelly")
print(b)




