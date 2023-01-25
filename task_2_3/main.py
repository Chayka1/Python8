from task_2_3.Customers import Customers


name = input('Введите имя: ')
address = input('Введите адрес: ')
phone_nums = input('Введите номер телефона: ')
bool_list = int(input('Хотите ли вы быть в рассылке? \nДля ответа да нажмите 1 \nДля ответа нет отпрате оюбое число: '))
custom = Customers(name, address, phone_nums, bool_list)

mailing_list = []

if custom.bool_list == 1:
    mailing_list.append(custom)
    print('Вас добвлено в рассылку!')
else:
    print('Вас не добавлено в рассылку!')

print(mailing_list)


