import os
import csv
import yaml

print(os.getcwd())

# with open('.csv/kp_data_delimiter.csv') as f:
#     f_read = csv.reader(f, delimiter='!')
#     for line in f_read:
#         print(line)
#
# with open('.kp_data.csv') as f:
#     f_read = csv.DictReader(f)
#     for line in f_read:
#         print(line)
#         print(line['hostname'], line['model'])
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['kp1', 'Cisco', '2960', 'Moscow'],
#         ['kp2', 'Cisco', '2960', 'Novosibirsk'],
#         ['kp3', 'Cisco', '2960', 'Kazan'],
#         ['kp4', 'Cisco', '2960', 'Tomsk']]
#
# with open('kp_data_write1.csv', 'w', newline='') as f:
#     f_writer = csv.writer(f)
#     for line in data:
#         f_writer.writerow(line)
#
# with open('kp_data_write1.csv') as f:
#     print(f.read())
#
# # with open('kp_data_write1.csv') as f:
# #     f_read = csv.reader(f)
# #     for line in f_read:
# #         print(line)
#
# data2 = [
#     {'hostname': 'kp1', 'vendor': 'Cisco', 'model': '2960', 'location': 'Moscow'},
#     {'hostname': 'kp2', 'vendor': 'Cisco', 'model': '2960', 'location': 'Novosibirsk'},
#     {'hostname': 'kp3', 'vendor': 'Cisco', 'model': '2960', 'location': 'Kazan'},
#     {'hostname': 'kp4', 'vendor': 'Cisco', 'model': '2960', 'location': 'Tomsk'}
# ]
#
# with open('kp_data_dictwrite.csv', 'w', newline='') as f:
#     f_writer = csv.DictWriter(f, fieldnames=list(data2[0].keys()))
#     f_writer.writeheader()
#     for d in data2:
#         f_writer.writerow(d)
#
# with open('kp_data_dictwrite.csv') as f:
#     print(f.read())



