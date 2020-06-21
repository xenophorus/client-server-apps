from socket import SOCK_STREAM, socket

sock = socket(type=SOCK_STREAM)
msg = 'Hello, world!'.encode('utf-8')
sock.connect(('127.0.0.1', 9090))
sock.send(msg)

data = sock.recv(1024)
sock.close()

print(data.decode('utf-8'))
