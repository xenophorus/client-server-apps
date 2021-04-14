import select

from socket import SOCK_STREAM, AF_INET, socket

from lib.decorators import log_dec
from lib.funx import *
from lib.logger import *


def read_requests(r_clients, all_clients):
    responses = {}
    for sock in r_clients:
        try:
            data = sock.recv(1024)
            responses[sock] = data.decode('utf-8')
            log.debug(f'data = {responses[sock]}')
        except Exception as e:
            log.error(f'Клиент {sock.fileno()} {sock.getpeername()} отключился\n\t\t{e}')
            all_clients.remove(sock)
    return responses


def write_responses(requests, w_clients, all_clients):
    # print(f'\t\t\t{requests}\n\n\t\t\t{all_clients}\n\n\t\t\t{w_clients}')
    for sock in all_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                for i in w_clients:
                    create_message('message sent')
                    i.send(resp)
            except Exception as e:
                print(e)
                log.error(f'Клиент {sock.fileno()} {sock.getpeername()} отключился\n\t\t{e}')
                sock.close()
                all_clients.remove(sock)


@log_dec
def mainloop(address=('127.0.0.1', 9090)):
    clients = []
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(1)

    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            # log.error(f'{e}')
            pass
        else:
            print("Получен запрос на соединение с %s" % str(addr))
            log.info(f'Получен запрос на соединение с {str(addr)}')
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except Exception as e:
                # log.error(f'{e}')
                pass

            requests = read_requests(r, clients)
            if requests:
                write_responses(requests, w, clients)


@log_dec
def main(args):
    log.info('server started')
    if len(args) > 1:
        mainloop(parse_args(args[1:]))
    else:
        mainloop(('127.0.0.1', 9090))


if __name__ == '__main__':
    log.info('server started')
    main(sys.argv)

