from task_2_2.Employee import Employee


class ProductionWorker(Employee):
    def __init__(self, name, id_num, num, pay_rate):
        Employee.__init__(self, name, id_num)
        self.__pay_rate = pay_rate
        self.__num = num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def set_num(self, num):
        self.__num = num

    def get_pay_rate(self):
        return self.__pay_rate

    def get_num(self):
        return self.__num

    def __str__(self):
        return f'Имя: {self.get_name()}\n' \
               f'ID: {self.get_id_num()}\n' \
               f'Смена: {self.get_num()}\n' \
               f'Почасовая ставка: {self.get_pay_rate()}'
