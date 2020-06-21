from socket import SOCK_STREAM, socket

sock = socket(type=SOCK_STREAM)
sock.bind(('127.0.0.1', 9090))
sock.listen(5)
conn, addr = sock.accept()

print(f'Connection established {addr}')

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())
finally:
    conn.close()
