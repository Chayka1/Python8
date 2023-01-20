def task_1_1():
    class Dog:
        def __init__(self, age):
            self.__age = age

        def set_age(self, age):
            self.__age = age

        def get_age(self):
            return self.__age

    class Poodle(Dog):
        def __init__(self, age, name):
            Dog.__init__(self, age)
            self.__name = name

        def set_name(self, name):
            self.__name = name

        def get_name(self):
            return self.__name

    dog = Poodle(10, 'Пушок')
    print(f'Имя пуделя: {dog.get_name()}\n'
          f'Возраст: {dog.get_age()}')


if __name__ == '__main__':
    task_1_1()
