# from socket import SOCK_STREAM, socket
#
# sock = socket(type=SOCK_STREAM)
# sock.bind(('192.168.1.67', 9090))
# sock.listen(5)
# conn, addr = sock.accept()
#
# print(f'Connection established {addr}')
#
# try:
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             break
#         conn.send(data.upper())
# finally:
#     conn.close()

from socket import SOCK_DGRAM, socket

sock = socket(type=SOCK_DGRAM)
sock.bind(('127.0.0.1', 9090))

try:
    while True:
        msg, addr = sock.recvfrom(1024)
        print(msg.decode('utf-8'))
        ans = 'Hello, client!'
        sock.sendto(ans.encode('utf-8'), addr)

finally:
    sock.close()
