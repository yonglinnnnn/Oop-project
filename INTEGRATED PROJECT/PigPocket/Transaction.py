class Transaction():
    def __init__(self,name,date,bank_details,transaction_details,deposit,withdraw):
        self.__name=name
        self.__date=date
        self.__bank_details=bank_details
        self.__transaction_details=transaction_details
        self.__deposit=deposit
        self.__withdraw=withdraw

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_bank_details(self):
        return self.__bank_details

    def get_transaction_details(self):
        return self.__transaction_details

    def get_deposit(self):
        if self.__deposit.lower()=="none":
            return self.__deposit
        else:
            r="%0.2f"%float(self.__deposit)
            return r


    def get_withdraw(self):
        if self.__withdraw.lower()=="none\n" or self.__withdraw.lower()=="none":
            return self.__withdraw

        else:
            r = "%0.2f" % float(self.__withdraw)
            return r
