from task_1_1.Dog import Dog


class Poodle(Dog):
    def __init__(self, age, name):
        Dog.__init__(self, age)
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f'Имя пуделя: {self.get_name()}\n' \
               f'Возраст: {self.get_age()}'
