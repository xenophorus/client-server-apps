import yaml

# -------------------------------------------------------------

# считываем данные из файла
with open('data_read.yaml') as f_n:
    f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)

print(f_n_content)

# -------------------------------------------------------------

# записываем объекты python в файл yaml
action_list = ['msg_1',
               'msg_2',
               'msg_3']

to_list = ['account_1',
           'account_2',
           'account_3']

data_to_yaml = {'action': action_list, 'to': to_list}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n)

# -------------------------------------------------------------
