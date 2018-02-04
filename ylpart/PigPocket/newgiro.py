class NewGiroUser:
    def __init__(self, name, bankno, amount, payto, specify, date, category,total, month):
        self.__name = name
        self.__bankno = bankno
        self.__amount = amount
        self.__payto = payto
        self.__specify = specify
        self.__date = date
        self.__category = category
        self.__total=total
        self.__month = month

    def get_name(self):
        return self.__name

    def get_bankno(self):
        return self.__bankno

    def get_amount(self):
        return self.__amount

    def get_payto(self):
        return self.__payto

    def get_specify(self):
        return self.__specify

    def get_date(self):
        return self.__date

    def get_category(self):
        return self.__category


    def get_total(self):
        return self.__total

    def get_month(self):
        return self.__month

