import sys
import json
import time
from socket import SOCK_STREAM, socket
import chardet
import funx


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


def create_client(addr):
    s = socket(type=SOCK_STREAM)
    s.connect(addr)

    while True:
        message = create_message()
        msg = json.dumps(message).encode('utf-8')
        s.send(msg)
        answer, addr = s.recvfrom(1024)
        print(answer.decode('utf-8'))


def start(args):
    if len(args) > 1:
        funx.parse_args(args[1:])
    else:
        create_client(('127.0.0.1', 9090))


start(sys.argv)
