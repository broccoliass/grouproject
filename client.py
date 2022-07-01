import socket
import sys

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

tab = input("Enter table number: ")
cSocket.send(str.encode(tab)) 

menu = cSocket.recv(SIZE)
print(menu.decode(FORMAT))

while True:

    opt = input("\nSelect Your Menu [Code Menu]\nEnter [1] to view menu\nEnter [2] to view list order\nEnter [3] to exit\n> ")

    if opt == '1':
        qty = '0'

    if opt == '2':
        qty = '0'
        Input = opt + ":" + qty
        cSocket.send(str.encode(Input))
        Response = cSocket.recv(SIZE)
        print('\nLIST ORDER FOR TABLE ' + tab)
        print(Response.decode(FORMAT))

    elif opt == '3':
        qty = '0'
        cSocket.send(str.encode(Input))
        Response = cScoket.recv(SIZE)
        print(Response.decode(FORMAT))
        break
    else:
        qty = input("Quantity: ")
        opt = opt.upper()

    Input = opt + ":" + qty
    cSocket.send(str.encode(Input))
    Response = cSocket.recv(SIZE)
    print(Response.decode(FORMAT))


cSocket.close()

