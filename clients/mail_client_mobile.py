import socket, sl4a

def Mail():
    host = '193.157.210.105'
    port = 60002
    droid = sl4a.Android()
    s = socket.socket()
    s.connect((host,port))
    s.send('mail,'.encode())
    message = s.recv(1024).decode() 
    droid.makeToast(message)
    s.close()

if __name__=='__main__':
    Mail()
