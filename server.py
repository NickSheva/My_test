import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.159', 1119))
s.listen(5)
print('Сервер запущен')
flag = True

while flag:
    try:
        client, addr = s.accept()

    except KeyboardInterrupt:
        s.close()
        break
    else:
        print(f'Connection from {addr} has been established')
        client.send(bytes("Welcom to the server", "utf-8"))
s.close()