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

greet = cSocket.recv(SIZE)               #recv greet
print (greet.decode(FORMAT))

tab = input("Enter table number: ")
cSocket.send(str.encode(tab))            #send table number

menu = cSocket.recv(SIZE)                #recv menu
print(menu.decode(FORMAT))

while True:
    try:
        opt = input("\nSelect Your Menu [Code Menu]\nEnter [1] to view menu\nEnter [2] to view list order\nEnter [3] to exit\n> ")

        if opt == '1':
            qty = '0'

        elif opt == '2':
            qty = '0'
            print('\nLIST ORDER FOR TABLE ' + tab)

        elif opt == '3':
            qty = '0'
            cSocket.send(str.encode(Input))        #send input to exit and break
            Response = cScoket.recv(SIZE)          #recv goodbye message
            print(Response.decode(FORMAT))
            break

        else:
            qty = input("Quantity: ")
            opt = opt.upper()

        Input = opt + ":" + qty
        cSocket.send(str.encode(Input))            #send input
        Response = cSocket.recv(SIZE)              #recv response of option 1, 2 and menu order
        print(Response.decode(FORMAT))

    except KeyboardInterrupt:
        print('\nCtrl + C is pressed, Lost Connection')
        sys.exit()

cSocket.close()

