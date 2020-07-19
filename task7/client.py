from socket import SOCK_STREAM, AF_INET, socket
from lib.decorators import log_dec
from lib.funx import *
from lib.logger import *


def set_msg():
    return input('Enter your message:\n')


@log_dec
def decfn():  # функция исключительно для поверки работы декоратора
    pass


@log_dec
def mainloop(address):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            message = create_message(set_msg())
            if list(message.values())[-1] == ':quit':
                break

            msg = jsoncode(message, 'enc')
            try:
                sock.send(msg)
                data = sock.recv(1024)

                log.info(f'{data} received')
                decfn()
            except OSError as e:
                log.critical(f'Something wrong. No answer from server.\n\t\t{e}')


@log_dec
def main(args):
    log.info('client started')
    if len(args) > 1:
        mainloop(parse_args(args[1:]))
    else:
        mainloop(('127.0.0.1', 9090))


if __name__ == '__main__':
    main(sys.argv)
