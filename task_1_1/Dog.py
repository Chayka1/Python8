class Dog:
    def __init__(self, age):
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
