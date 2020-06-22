import sys
import json
import time
from socket import SOCK_STREAM, socket
import chardet


def create_message():
    def set_time():
        return time.asctime()

    def set_msg():
        return input('Enter your message:\n')

    def get_encoding(msgs):
        msgs = str(frozenset(msgs)).encode()
        return chardet.detect(msgs).get('encoding')

    msg_action = 'message'
    msg_time = set_time()
    msg_to_user = 'Alex'
    msg_from_user = 'Nick'
    msg = set_msg()
    msg_encoding = get_encoding(msg)

    message = dict(action=msg_action, time=msg_time, to=msg_to_user,
                   from_user=msg_from_user, message=msg, enc=msg_encoding)

    return message


def create_client(server, port):
    s = socket(type=SOCK_STREAM)
    s.connect((server, port))

    while True:
        message = create_message()
        msg = json.dumps(message).encode('utf-8')
        s.send(msg)
        answer, addr = s.recvfrom(1024)
        print(answer.decode('utf-8'))


def show_help():
    print('Possible parameters:'
          '\n\t-h: server host'
          '\n\t-p: server port'
          '\n\t-? or help: show this help'
          '\n\t default host:port is 127.0.0.1:9090')


def parse_args(args):
    server, port = '127.0.0.1', '9090'
    for i in range(len(args)):
        if args[i] == '-p':
            port = args[i + 1]
        elif args[i] == '-h':
            server = args[i + 1]
        elif args[i] == '-?':
            show_help()
            break
        else:
            if i % 2 == 0:
                print(f'{args[i]} is incorrect argument. Skipped')
    create_client(server, port)


def start(args):
    if len(args) > 1:
        parse_args(args[1:])
    else:
        create_client('127.0.0.1', 9090)


start(sys.argv)
