class showGiroDetails:
    def __init__(self, name, amount, payto, date , specify, success , monthdiff):
        self.__name = name
        self.__amount = amount
        self.__payto = payto
        self.__date = date
        self.__specify=specify
        self.__success =success
        self.__currentmonth = 0
        self.__monthdiff = monthdiff

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_payto(self):
        return self.__payto

    def get_date(self):
        return self.__date

    def get_specify(self):
        return self.__specify

    def get_sucess(self):
        return self.__success

    def get_currentmonth(self):
        return self.__currentmonth

    def get_monthdiff(self):
        return self.__monthdiff


