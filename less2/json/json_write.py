import json

# -------------------------------------------------------------

dict_to_json = {
    'action': 'msg',
    'to': 'account_name',
    'from': 'account_name',
    'encoding': 'ascii',
    'message': 'message',
    'number': 13,
}

# преобразование python-объекта (словаря) в json-строку
json_str = json.dumps(dict_to_json)
print(json_str)

# -------------------------------------------------------------

# запись python-объекта в файл в формате json
with open('mes_example_write_1.json', 'w') as f_n:
    json.dump(dict_to_json, f_n)

# -------------------------------------------------------------

# использование дополнительных параметров записи
with open('mes_example_write_2.json', 'w') as f_n:
    json.dump(dict_to_json, f_n, sort_keys=True, indent=2)

# -------------------------------------------------------------
