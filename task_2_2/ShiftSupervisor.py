from task_2_2.Employee import Employee


class ShiftSupervisor(Employee):
    def __init__(self, name, id_num, annual_salary, annual_bonus):
        Employee.__init__(self, name, id_num)
        self.__annual_bonus = annual_bonus
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def __str__(self):
        return f'Name: {self.get_name()}\n' \
               f'ID: {self.get_id_num()}\n' \
               f'Annual salary: {self.get_annual_salary()}\n' \
               f'Annual bonus: {self.get_annual_bonus()}'
