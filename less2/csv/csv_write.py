import csv

# -------------------------------------------------------------

# простая запись данных в файл .csv и вывод результата
data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosibirsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('kp_data_write_1.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n)
    for row in data:
        f_n_writer.writerow(row)

with open('kp_data_write_1.csv') as f_n:
    print(f_n.read())
    print(type(f_n.read()))

# -------------------------------------------------------------

# программная установка записи файлы с кавычками в строках
with open('kp_data_write_2.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        f_n_writer.writerow(row)

with open('kp_data_write_2.csv') as f_n:
    print(f_n.read())

# -------------------------------------------------------------

# использование метода writerows
with open('kp_data_write_3.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
    f_n_writer.writerows(data)

with open('kp_data_write_3.csv') as f_n:
    print(f_n.read())

# -------------------------------------------------------------

# запись словаря в формат .csv
data = [{'hostname': 'kp1',
         'location': 'Moscow',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp2',
         'location': 'Novosibirsk',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp3',
         'location': 'Kazan',
         'model': '2960',
         'vendor': 'Cisco'},
        {'hostname': 'kp4',
         'location': 'Tomsk',
         'model': '2960',
         'vendor': 'Cisco'}]

with open('kp_data_dictwriter.csv', 'w') as f_n:
    f_n_writer = csv.DictWriter(f_n, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    f_n_writer.writeheader()
    for d in data:
        f_n_writer.writerow(d)

# -------------------------------------------------------------
