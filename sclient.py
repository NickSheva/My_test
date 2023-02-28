import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1119))

flag = True
while flag:
    client.send(input('Me: ').encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        flag = False
    else:
        print(msg)
client.close()
server.close()



































import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9876))
name = input('Enter your name: ')
flag = True
while flag:
    client.send(input(name).encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        flag == False
    else:
        print(msg)

client.close()
server.close()