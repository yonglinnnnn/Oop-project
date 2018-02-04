class Accounts:

    def __init__(self,bank,account_no,type):
        self.__bank = bank
        self.__account_no = account_no
        self.__type = type

    def get_bank(self):
        return self.__bank

    def get_account_no(self):
        return self.__account_no

    def get_type(self):
        return self.__type
