# from socket import SOCK_STREAM, socket

# sock = socket(type=SOCK_STREAM)
# msg = 'Hello, world!'.encode('utf-8')
# sock.connect(('192.168.1.42', 9090))
# sock.send(msg)
#
# data = sock.recv(1024)
# sock.close()
#
# print(data.decode('utf-8'))

from socket import SOCK_DGRAM, socket

sock = socket(type=SOCK_DGRAM)

try:
    while True:
        data = 'Hello, server!'
        sock.sendto(data.encode('utf-8'), ('localhost', 9090))
        msg, addr = sock.recvfrom(1024)
        print(msg.decode('utf-8'))
finally:
    sock.close()
