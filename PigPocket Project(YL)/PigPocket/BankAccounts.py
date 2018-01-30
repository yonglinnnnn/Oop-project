class BankAccounts():
    def __init__(self, bankBranch, bankNum, accountType, interestRate, originalaccountBal, accountBal):
        self.__bankBranch = bankBranch
        self.__bankNum = bankNum
        self.__accountType = accountType
        self.__interestRate = interestRate
        self.__originalaccountBal = originalaccountBal
        self.__accountBal = accountBal

    def get_bankBranch(self):
        return self.__bankBranch
    def get_bankNum(self):
        return self.__bankNum
    def get_accountType(self):
        return self.__accountType
    def get_interestRate(self):
        return self.__interestRate
    def get_originalaccountBal(self):
        return self.__originalaccountBal
    def get_accountBal(self):
        return self.__accountBal

    def set_bankBranch(self, bankBranch):
        self.__bankBranch = bankBranch
    def set_bankNum(self, bankNum):
        self.__bankNum = bankNum
    def set_accountType(self, accountType):
        self.__accountType = accountType
    def set_interestRate(self, interestRate):
        self.__interestRate = interestRate
    def set_originalaccountBal(self, originalaccountBal):
        self.__originalaccountBal = originalaccountBal
    def set_accountBal(self, accountBal):
        self.__accountBal = accountBal
