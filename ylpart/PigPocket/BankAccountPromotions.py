class BankAccountPromotions:
    def __init__(self, bankBranch, accountType, startDate, endDate, promoName, promoURL, promoPic):
        self.__bankBranch = bankBranch
        self.__accountType = accountType
        self.__startDate = startDate
        self.__endDate = endDate
        self.__promoName = promoName
        self.__promoURL = promoURL
        self.__promoPic = promoPic


    def get_bankBranch(self):
        return self.__bankBranch
    def get_accountType(self):
        return self.__accountType
    def get_startDate(self):
        return self.__startDate
    def get_endDate(self):
        return self.__endDate
    def get_promoName(self):
        return self.__promoName
    def get_promoURL(self):
        return self.__promoURL
    def get_promoPic(self):
        return self.__promoPic

    def set_startDate(self, newstartDate):
        self.__startDate = newstartDate
    def set_endDate(self, newendDate):
        self.__endDate = newendDate
