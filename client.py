import socket

FORMAT = "utf-8"
SIZE = 2048

cSocket = socket.socket()
host = '192.168.125.3'
port = 8888

print('Waiting for connection')
try:
        cSocket.connect((host, port))
except socket.error as e:
        print(str(e))

greet = cSocket.recv(SIZE)
print (greet.decode(FORMAT))

menu = cSocket.recv(SIZE)
print(menu.decode(FORMAT))


