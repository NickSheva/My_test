import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1119))
server.listen()

client, addr = server.accept()
flag = True
while flag:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        flag = False
    else:
        print(msg)
    client.send(input('Server: ').encode('utf-8'))
