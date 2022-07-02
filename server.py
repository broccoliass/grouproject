import socket
import sys
import os
from multiprocessing import Process

FORMAT = 'utf-8'
SIZE = 2048

def process_start(s_sock):

    s_sock.send(str.encode('\n\t\t\tWELCOME TO MAID CAFE\t\t\t\n'))     #send greet

    text_file = open("menu.txt", "r")
    data = text_file.read()
    text_file.close()

    num = s_sock.recv(SIZE)              #recv table number
    tab = num.decode(FORMAT)

    s_sock.send(data.encode(FORMAT))     #send menu
    print('Customer making an order')

    while True:

        input = s_sock.recv(SIZE)        #recv option, quantity
        data = input.decode(FORMAT)
        
        try:
            menu, num  = data.split(":")
            opt = str(menu)
            qty = int(num)
            prc = float(0)

            if opt[0] == '1':
                text_file = open("menu.txt", "r")
                data = text_file.read()
                text_file.close()
                
                s_sock.send(data.encode(FORMAT))        #send menu 

            elif opt[0] == '2':
                text_file = open("order.txt", "r") 
                data = text_file.read()
                text_file.close()
              
                s_sock.send(data.encode(FORMAT))       #send list order

            elif opt[0] == '3':
                bye = '\nYour order has been sent to the kitchen and ready to serve..\nThank you for your order :)\n'
                s_sock.send(bye.encode(FORMAT))        #send goodbye message

                text_file = open("order.txt", "r")
                data = text_file.read()
                text_file.close()

                print('\nORDER RECEIVED FOR TABLE ' + tab)     #display all order after client exit
                print(data)
                os.remove("order.txt")                         #remove file for next order when exit
            else:
                if opt[0]  == 'A':
                    opt = 'Nasi Lemak Kukus'
                    prc = 5.3
                    ans = qty * (prc)
                elif opt[0] == 'B':
                    opt = 'Soto'
                    prc = 6
                    ans = qty * (prc)
                elif opt[0] == 'C':
                    opt = 'Sizzling'
                    prc = 7
                    ans = qty * (prc)
                elif opt[0] == 'D':
                    opt = 'Nasi Kerabu'
                    prc = 6
                    ans = qty * (prc)
                elif opt[0] == 'E':
                    opt = 'Nasi Goreng'
                    prc = 5
                    ans = qty * (prc)
                elif opt[0] == 'F':
                    opt = 'Mi Goreng'
                    prc = 3
                    ans = qty * (prc)
                elif opt[0] == 'G':
                    opt = 'Bakso'
                    prc = 3.50
                    ans = qty * (prc)
                elif opt[0] == 'H':
                    opt = 'Lontong'
                    prc = 3.80
                    ans = qty * (prc)
                elif opt[0] == 'I':
                    opt = 'Western Mixed Platter'
                    prc = 7.80
                    ans = qty * (prc)
                elif opt[0] == 'J':
                    opt = 'BBQ Chicken Wrap'
                    prc = 6.70
                    ans = qty * (prc)
                elif opt[0] == 'K':
                    opt = 'Fish n Chip'
                    prc = 7
                    ans = qty * (prc)
                elif opt[0] == 'L':
                    opt = 'Roti Canai'
                    prc = 5
                    ans = qty * (prc)
                elif opt[0] == 'M':
                    opt = 'White Coffee'
                    prc = 5
                    ans = qty * (prc)
                elif opt[0] == 'N':
                    opt = 'Chocolate'#
                    prc = 4
                    ans = qty * (prc)
                elif opt[0] == 'O':
                    opt = 'Double Enriched Chocolate'
                    prc = 6.30
                    ans = qty * (prc)
                elif opt[0] == 'P':
                    opt = 'White Coffee Hazelnut Freezy'
                    prc = 5.80
                    ans = qty * (prc)
                elif opt[0] == 'Q':
                    opt = 'Milo'
                    prc = 3.20
                    ans = qty * (prc)
                elif opt[0] == 'R':
                    opt = 'Mineral Water'
                    prc = 1.20
                    ans = qty * (prc)
                elif opt[0] == 'S':
                    opt = 'Signature Ice Cream'
                    prc = 4
                    ans = qty * (prc)
                elif opt[0] == 'T':
                    opt = 'Ice Kacang'
                    prc = 4.70
                    ans = qty * (prc)
                else:
                    sendtoCli = ('Sorry, the code is not available in the menu')

                sendtoCli = (str(opt)+ '.... RM'+ str(prc)+ ' ['+ str(qty) + ']: RM' + str(ans))
                print(sendtoCli)                                 #print for each order

                f = open ('order.txt','a')
                f.write(str(opt)+ '.... RM'+ str(prc)+ ' ['+ str(qty) + ']: RM' + str(ans) + '\n')
                f.close()            
                s_sock.send(str.encode(str(sendtoCli)))          #send each complete order

        except:
            print ('Hello kitchen, get ready to serve!')         #notify the kitchen to serve
            break

        if not data:
            break

    f.close()
    s_sock.close() 

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',8888))
    print('Waiting for cutomer')
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                print(f'[+] {s_addr} Connected')
                p1 = Process(target=process_start, args=(s_sock,))
                p1.start()
            except socket.error:
                print('got a socket error')
    except KeyboardInterrupt:
        print('\nCtrl + C is pressed, Server Close')
        sys.exit()
    except Exception as e:        
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	s.close()

