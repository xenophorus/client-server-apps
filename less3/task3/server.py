import sys
import json
from socket import SOCK_STREAM, socket
from task3 import funx


def decoder(data):
    data = json.loads(data.decode('utf-8'))
    time = data.get('time')
    to = data.get('to')
    from_user = data.get('from_user')
    message = data.get('message')
    print(f'{time}: from {from_user} to {to}\n\t'
          f'{message}')


def create_server(addr):
    s = socket(type=SOCK_STREAM)
    s.bind(addr)
    s.listen(5)
    conn, addr = s.accept()
    try:
        while True:
            data = conn.recv(1024)
            decoder(data)
            ans = 'Message received'.encode('utf-8')
            conn.send(ans)
    finally:
        conn.close()


def start(args):
    if len(args) > 1:
        create_server(funx.parse_args(args[1:]))
    else:
        create_server(('127.0.0.1', 9090))


start(sys.argv)
