from socket import SOCK_STREAM, AF_INET, socket

from lib.decorators import log_dec
from lib.funx import *
from lib.logger import *
from threading import Thread
from lib.classes import Message


def sender(sock, msg):
    try:
        sock.send(msg)
        log.info(f'{msg} sent')
    except OSError as e:
        log.critical(f'Something wrong. No answer from server.\n\t\t{e}')


def get_message(sock):
    try:
        data = sock.recv(1024)
        msg = Message()
        Message.decode(self=msg, data=data)
        print(f'{msg.from_user} at {msg.time_date} said to {msg.to_user}:\n\t{msg.message}')
    except OSError as e:
        log.critical(f'Something wrong. No answer from server.\n\t\t{e}')
        sys.exit()


def get_loop(sock, client_name):
    while True:
        try:
            data = sock.recv(1024)
            msg = Message()
            Message.decode(self=msg, data=data)
            if msg.to_user == client_name or msg.to_user == 'all':
                print(f'{msg.from_user} at {msg.time_date} said to {msg.to_user}:\n\t{msg.message}')
        except OSError as e:
            log.critical(f'Something wrong. No answer from server.\n\t\t{e}')
            sys.exit()


def send_loop(*args):
    sock, client_name = args
    while True:
        key = input(f'Введите команду: "q" для выхода, "m" для нового сообщения: ')
        if key == 'q':
            sys.exit()
        elif key == 'm':
            message = Message()
            message.create('message', client_name)
            sender(sock, message.encode())


@log_dec
def mainloop(address, client_name):
    with socket(AF_INET, SOCK_STREAM) as sock:
        print(address)
        sock.connect(address)
        # i_mess = Message()  # Это задел для классов
        # i_mess.action = 'introduce'
        # i_mess.from_user = client_name
        # sender(sock, i_mess.encode())
        thr1 = Thread(target=get_loop, args=(sock, client_name))
        thr1.start()
        send_loop(sock, client_name)


@log_dec
def main(*args):
    log.info('client started')
    address, client_name = parse_args(args[1:])
    print(address, client_name)

    mainloop(address, client_name)


if __name__ == '__main__':
    main(sys.argv)