from task_2_3.Person import Person


class Customers(Person):
    def __init__(self, name, address, phone_nums, bool_list):
        Person.__init__(self, name, address, phone_nums)
        self.bool_list = bool_list

    def __str__(self):
        return f'Name: {self.get_name()}\n' \
               f'Address: {self.get_address()}\n' \
               f'Phone number: {self.get_phone_nums()}'

