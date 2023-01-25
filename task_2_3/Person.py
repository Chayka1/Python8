class Person:
    def __init__(self, name, address, phone_nums):
        self.__phone_nums = phone_nums
        self.__address = address
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_nums(self, phone_nums):
        self.__phone_nums = phone_nums

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_nums(self):
        return self.__phone_nums

