import sys
import json
from socket import SOCK_STREAM, socket


def create_server(host, port):
    s = socket(type=SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    try:
        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            code = 200
            ans = 'Message from {} to {} received'.encode('utf-8')
            conn.sendto(ans, addr)
    finally:
        conn.close()


def show_help():
    print('Possible parameters:'
          '\n\t-h: host'
          '\n\t-p: port'
          '\n\t-? or help: show this help'
          '\n\t default host:port is 127.0.0.1:9090')


def parse_args(args):
    host, port = '127.0.0.1', '9090'
    for i in range(len(args)):
        if args[i] == '-p':
            port = args[i + 1]
        elif args[i] == '-h':
            host = args[i + 1]
        elif args[i] == '-?':
            show_help()
            break
        else:
            if i % 2 == 0:
                print(f'{args[i]} is incorrect argument. Skipped')
    create_server(host, port)


def start(args):
    if len(args) > 1:
        parse_args(args[1:])
    else:
        create_server('127.0.0.1', 9090)


start(sys.argv)
