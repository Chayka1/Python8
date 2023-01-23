class Employee:
    def __init__(self, name, id_num):
        self.__name = name
        self.__id_num = id_num

    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

