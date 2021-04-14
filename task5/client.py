import sys
import time
import chardet
import json
from socket import SOCK_STREAM, socket

import funx

import client_logger


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
    client_logger.LOG.debug(f'message complete, time:{msg_time}, enc:{msg_encoding}')
    return message


def create_client(addr):
    s = socket(type=SOCK_STREAM)
    try:
        s.connect(addr)
        client_logger.LOG.info('Connection established')
    except ConnectionRefusedError:
        client_logger.LOG.critical('Connection refused!')

    while True:
        message = create_message()
        msg = json.dumps(message).encode('utf-8')
        try:
            s.send(msg)
            client_logger.LOG.info('message sent')
            answer, addr = s.recvfrom(1024)
            client_logger.LOG.info(f'answer received from {addr}:\n\t{answer.decode("utf-8")}')
        except OSError:
            client_logger.LOG.critical('Something wrong. No answer from server.')


def main(args):
    if len(args) > 1:
        funx.parse_args(args[1:])
    else:
        create_client(('127.0.0.1', 9090))


if __name__ == '__main__':
    client_logger.LOG.info('client started')
    main(sys.argv)
