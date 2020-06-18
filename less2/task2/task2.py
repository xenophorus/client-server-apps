# Задание на закрепление знаний по модулю json. Есть файл orders в формате
# JSON с информацией о заказах. Написать скрипт, автоматизирующий его
# заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров
# — товар (item), количество (quantity), цена (price), покупатель (buyer),
# дата (date). Функция должна предусматривать запись данных в виде словаря
# в файл orders.json. При записи данных указать величину отступа в 4
# пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    my_dict = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('./files/orders.json', 'r') as jfile:
        content = json.load(jfile)
        with open('./files/orders.json', 'w', encoding='utf-8') as jfile1:
            content['orders'].append(my_dict)
            json.dump(content, jfile1, indent=4)


write_order_to_json('CPU', 12, 10000, 'Ingrid', '2020.06.15')
write_order_to_json('Motherboard', 15, 4000, 'Alex', '2020.06.15')
write_order_to_json('RAM', 4, 1200, 'Jacob', '2020.06.15')
write_order_to_json('Keyboard', 32, 1000, 'Nastya', '2020.06.15')

"""
Я его чуть модифицировал. 
"""
