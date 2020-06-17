import json

# -------------------------------------------------------------

# использование метода load для чтения json-файла
with open('mes_example_read.json') as f_n:
    obj = json.load(f_n)

for key, value in obj.items():
    print(f'key: {key}. value: {value}.')

# -------------------------------------------------------------

# использование метода loads для чтения json-строки
with open('mes_example_read.json') as f_n:
    f_n_content = f_n.read()
    obj = json.loads(f_n_content)

test = '{"action": "msg", "to": "account_name","from": "account_name", "encoding": "ascii", "message": "message"}'
test = json.loads(test)
print(type(test))

print(obj)

for key, value in obj.items():
    print(f'key: {key}. value: {value}.')

# -------------------------------------------------------------
