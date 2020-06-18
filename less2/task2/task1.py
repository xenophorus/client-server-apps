# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий
# выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и
# формирующий новый «отчетный» файл в формате CSV. Для этого:
#
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
# с данными, их открытие и считывание данных. В этой функции из считанных
# данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно
# получиться четыре списка — например, os_prod_list, os_name_list,
# os_code_list, os_type_list. В этой же функции создать главный список для
# хранения данных отчета — например, main_data — и поместить в него названия
# столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
# «Код продукта», «Тип системы». Значения для этих столбцов также оформить
# в виде списка и поместить в файл main_data (также для каждого файла);
#
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import os
import re
import csv
import chardet


def check_el(line):
    file_check = re.search(r'info_[\d]+\.txt', line)
    return file_check


def get_data(files):
    os_prod_list = []
    os_date_list = []
    os_code_list = []
    os_type_list = []

    def check_line(ln):
        if re.search(r'^Название[\w\s.:]+$', ln):
            os_prod_list.append(ln)
        if re.search(r'^Дата\s[\w:]+[\s]+[0-9.,:\s]+$', ln):
            os_date_list.append(ln)
        if re.search(r'^Код[\w:\s-]+$', ln):
            os_code_list.append(ln)
        if re.search(r'^Версия\sОС:[\s]+[\s\d\w.]+$', ln):
            os_type_list.append(ln)

    for file in files:
        with open('./files/' + file) as fl:
            for line in fl:
                check_line(line)

    print()


def start():
    files = list(filter(check_el, os.listdir('./files')))
    get_data(files)


start()
