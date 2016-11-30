import socket, sys, threading
from mail import read
from verdensdytt import store

class Server:

    def __init__(self):
        self.HOST = ''
        self.PORT = 60002
        self.s = self.startup()
        self.s.listen(10)

    def __call__(self):
        print("listening for connections")
        while 1:
            conn, addr = self.s.accept()
            print("opening connection {}".format(addr))
            t = threading.Thread(target=self.clientthread,args=(conn,addr))
            t.start()

    def startup(self):
        print("creating socket")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("binding socket with host: {} and port: {}".format(self.HOST,self.PORT))
            s.bind((self.HOST,self.PORT))
        except socket.error as msg:
            print(str(msg))
            sys.exit()
        return s


    def clientthread(self,conn,addr):
        while 1:
            try:
                data = conn.recv(1024).decode()
            except ConnectionResetError:
                print("connection lost")
                break

            if data=='mail':
                reply = read.read_mail()
                conn.sendall(reply.encode())
                break

            elif 'dytt' in data:
                data = data.split(',')
                print(data[0],data[1])
                try:
                    number = int(data[1])
                    printout = "verdensdytt: {}".format(number)
                    reply    = "Good job!".encode()
                    store.store(int(data[1]))
                except:
                    printout = "No number recieved"
                    reply    = "Fucker...".encode()

                print(printout)
                conn.sendall(reply)
                break

            if not data:
                break
    
        print("closing connection {}".format(addr))
        conn.close()

    

if __name__=='__main__':
    main = Server()
    main()
    main.s.close()
