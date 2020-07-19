from socket import SOCK_STREAM, AF_INET, socket
from lib.funx import *
from lib.logger import *


def mainloop(address):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            try:
                data = sock.recv(1024)
                print(decoder(data))
                log.info(f'{data} received')
            except OSError as e:
                log.critical(f'Something wrong. No answer from server.\n\t\t{e}')
                sys.exit()


def main(args):
    log.info('client started')
    if len(args) > 1:
        mainloop(parse_args(args[1:]))
    else:
        mainloop(('127.0.0.1', 9090))


if __name__ == '__main__':
    main(sys.argv)
