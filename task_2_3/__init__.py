from task_2_3.Customers import Customers

custom = Customers('Max', 'Brovary', '+380635478177', 1)

mailing_list = []

if custom.bool_list == 1:
    mailing_list.append(custom)
    print(mailing_list)
else:
    print(custom)

