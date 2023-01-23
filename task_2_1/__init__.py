from task_2_1.ProductionWorker import ProductionWorker

name_ = input('Введите имя сотрудника: ')
id_num_ = int(input('Введите ID сотрудника: '))
num_ = int(input('Введите номер смены 1 - дневная , 2 - ночная: '))
pay_rate_ = int(input('Введите почасовую ставку: '))

worker = ProductionWorker(name_, id_num_, num_, pay_rate_)
print(worker)
