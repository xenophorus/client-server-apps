import csv

# Простое чтение из файла kp_data.csv
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    for row in f_n_reader:
        print(row)

# Преобразование итератора в список
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(list(f_n_reader))

# Разделение строки заголовков от содержимого
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    f_n_headers = next(f_n_reader)
    print('Headers: ', f_n_headers)
    for row in f_n_reader:
        print(row)

# указания разделителя при чтении
with open('kp_data_delimiter.csv') as f_n:
    f_n_reader = csv.reader(f_n, delimiter='!')
    for row in f_n_reader:
        print(row)

# Вывод результата с помощью метода DictReader
with open('kp_data.csv') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row)
        print(row['hostname'], row['model'])
