class point():
    def __init__(self,name,point,reward,date):
        self.__name=name
        self.__point=point
        self.__reward=reward
        self.__date=date


    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_point(self):
        return self.__point

    def set_point(self,point):
        self.__point=point

    def get_reward(self):
        return self.__reward

    def set_reward(self,reward):
        self.__reward=reward


    def get_date(self):
        return self.__date
    def set_date(self,date):
        self.__date=date


