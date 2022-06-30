import socket
from multiprocessing import Process

FORMAT = 'utf-8'
SIZE = 2048

def process_start(s_sock):

  s_sock.send(str.encode('\n\t\t\tWELCOME TO MAID CAFE\t\t\t\n'))

  text_file = open("menu.txt", "r")
  data = text_file.read()
  text_file.close()

  num = s_sock.recv(SIZE)
  tab = num.decode(FORMAT)

  s_sock.send(data.encode(FORMAT))
  print('Customer making an order')

  while True:

        input = s_sock.recv(SIZE)              
        data = input.decode(FORMAT)
        
        try:
            menu, num  = data.split(":")
            opt = str(menu)
            qty = int(num)
            prc = float(0)

                s_sock.send(data.encode(FORMAT))  

            if opt[0] == '1':
                text_file = open("order.txt", "r") 
                data = text_file.read()
                text_file.close()

                s_sock.send(data.encode(FORMAT))
         except:
                print ('Hello kitchen, get ready to serve!')  
                break

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',8888))
    print('Listening...')
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
    except Exception as e:        
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	s.close()

