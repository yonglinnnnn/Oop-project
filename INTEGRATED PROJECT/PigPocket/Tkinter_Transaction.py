import datetime
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import RetrievingProcess

user = input("Which user do you want to do the transaction(Steven/Kelly): ")

accountList = []
for accounts in RetrievingProcess.processUserDetails(user.capitalize()):
    accountList.append(accounts)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

dayNow = datetime.date.today().strftime("%d")
monthNow = datetime.datetime.now().month - 1
yearNow = datetime.date.today().strftime("%Y")


class StevenTransaction:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("ATM stimulation")
        self.main_window.minsize(width=300, height=300)
        self.main_window.maxsize(width=300, height=300)
        self.first_frame = tk.Frame()
        self.label1 = tk.Label(self.first_frame, text='Input account number ', width=20)
        self.text1 = tk.Entry(self.first_frame, width=15)
        self.button = tk.Button(self.first_frame, text='Enter', command=self.display)
        self.label1.pack(side='left')
        self.text1.pack(side='left')
        self.button.pack(side='left')
        self.first_frame.pack(side='top')
        tkinter.mainloop()

        self.__totalWithdrawal = 0
        self.__totalDeposit = 0

    def get_totalWithdrawal(self):
        return self.__totalWithdrawal
    def get_totalDeposit(self):
        return self.__totalDeposit

    def set_totalWithdrawal(self, totalWithdrawal):
        self.__totalWithdrawal = totalWithdrawal
    def set_totalDeposit(self, totalDeposit):
        self.__totalDeposit = totalDeposit

    def display(self):
        account = self.text1.get()
        try:
            user_file = open('file/' + user.capitalize(), 'w')
            for accounts in accountList:
                if account == accounts.get_bankNum():
                    print(accounts.get_bankNum())
                    print(accounts.get_accountBal())
                    tkinter.messagebox.showinfo('Response', 'You have selected bank account {}'.format(account))
                    while True:
                        transaction = tkinter.simpledialog.askstring("Response", "Do you wish to withdraw or deposit? ")
                        if transaction.lower() == "withdraw":
                            while True:
                                amount = tkinter.simpledialog.askstring("Response", "Withdraw amount? ")
                                try:
                                    amount = float(amount)
                                except ValueError:
                                    print('Error converting')
                                except TypeError:
                                    print('TypeError')
                                except:
                                    print('Unknown error')
                                else:
                                    if amount > 0:
                                        balance = float(accounts.get_accountBal())
                                        balance -= amount
                                        accounts.set_accountBal(balance)
                                        print(accounts.get_accountBal())
                                        tkinter.messagebox.showinfo('Response', '${} withdrawn.'.format(amount))
                                        try:
                                            bankTransFile = open("file/" + str(accounts.get_bankNum()), 'a')
                                            bankTransFile.writelines("%s,%s,%s,%s,%s,%.2f,%s,%s" %(user.capitalize(), (str(dayNow) + " " + months[monthNow] + " " + str(yearNow)), (accounts.get_bankBranch() + " " + accounts.get_bankNum()), transaction.capitalize(), "None", amount, months[monthNow], str(yearNow)+"\n"))
                                            bankTransFile.close()
                                            AllTrans=open("file/AllTransaction.txt","a")
                                            AllTrans.writelines("%s,%s,%s,%s,%s,%.2f,%s,%s" %(user.capitalize(), (str(dayNow) + " " + months[monthNow] + " " + str(yearNow)), (accounts.get_bankBranch() + " " + accounts.get_bankNum()), transaction.capitalize(), "None", amount, months[monthNow], str(yearNow)+"\n"))
                                            AllTrans.close()
                                        except IOError:
                                            print("File not found")
                                        except:
                                            print("Unknown error")
                                        break
                                    else:
                                        tkinter.messagebox.showinfo('Response', 'Invalid Amount. Please re-enter amount.')
                            break
                        elif transaction.lower() == "deposit":
                            while True:
                                amount = tkinter.simpledialog.askstring("Response", "Deposit amount? ")
                                try:
                                    amount = float(amount)
                                except ValueError:
                                    print('Error converting')
                                except TypeError:
                                    print('TypeError')
                                except:
                                    print('Unknown error')
                                else:
                                    if amount > 0:
                                        balance = float(accounts.get_accountBal())
                                        balance += amount
                                        accounts.set_accountBal(balance)
                                        print(accounts.get_accountBal())
                                        tkinter.messagebox.showinfo('Response', '${} deposited.'.format(amount))
                                        try:
                                            bankTransFile = open("file/" + str(accounts.get_bankNum()), 'a')
                                            bankTransFile.writelines("%s,%s,%s,%s,%.2f,%s, %s, %s" % (user.capitalize(), (str(dayNow) + " " + months[monthNow] + " " + str(yearNow)),(accounts.get_bankBranch() + " " + accounts.get_bankNum()),transaction.capitalize(), amount, "None", months[monthNow], str(yearNow)+"\n"))
                                            bankTransFile.close()
                                            AllTrans=open("file/AllTransaction.txt","a")
                                            AllTrans.writelines("%s,%s,%s,%s,%.2f,%s, %s, %s" % (user.capitalize(),(str(dayNow) + " " + months[monthNow] + " " + str(yearNow)),(accounts.get_bankBranch() + " " + accounts.get_bankNum()),transaction.capitalize(), amount, "None", months[monthNow], str(yearNow)+"\n"))
                                            AllTrans.close()
                                        except IOError:
                                            print("File not found")
                                        except:
                                            print("Unknown error")
                                        break
                                    else:
                                        tkinter.messagebox.showinfo('Response', 'Invalid Amount. Please re-enter amount.')
                            break
                        else:
                            tkinter.messagebox.showinfo('Response', 'Invalid transaction command.')
                accountDetails = accounts.get_bankBranch() + "," + accounts.get_bankNum() + "," + accounts.get_accountType() + "," + str(accounts.get_interestRate()) + "," + str(accounts.get_originalaccountBal()) + "," + str(accounts.get_accountBal()) + "\n"
                user_file.write(accountDetails)
            user_file.close()
        except IOError:
            print("File not found")
        except:
            print("Unknown error")

StevenTransaction()

