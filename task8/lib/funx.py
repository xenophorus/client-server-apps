import json
from lib.logger import *


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
    addr = (host, port)
    return addr


def jsoncode(data, command):
    if command == 'dec':
        return json.loads(data.decode('utf-8'))
    if command == 'enc':
        return json.dumps(data).encode('utf-8')


def decoder(data):
    ddata = jsoncode(data, 'dec')
    time_ = ddata.get('time')
    to = ddata.get('to')
    from_user = ddata.get('from_user')
    message = ddata.get('message')
    log.info(f'Message from {from_user} to {to} received at {time_} \n\t{message}')
    return [from_user, to, time_, message]


def create_message(msg, msg_from_user):
    msg_action = 'message'
    msg_time = time.asctime()
    msg_to_user = 'all'
    log.debug(f'message complete, time:{msg_time}')
    return dict(action=msg_action, time=msg_time, to=msg_to_user,
                from_user=msg_from_user, message=msg)
