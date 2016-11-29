import socket

class Mail:
    def __call__(self):
        host = '37.191.195.168'
        port = 60002
        s = socket.socket()
        s.connect((host,port))
        s.send('mail'.encode())
        message = s.recv(1024).decode() 
        print(message.strip())
        s.close()

if __name__=='__main__':
    test = Mail()
    test()
