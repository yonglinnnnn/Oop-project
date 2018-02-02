class Users:

    def __init__(self,name,nric,password):
        self.__NRIC = nric
        self.__Password = password
        self.__Name = name

    def get_nric(self):
        return self.__NRIC

    def get_password(self):
        return self.__Password

    def get_name(self):
        return self.__Name


