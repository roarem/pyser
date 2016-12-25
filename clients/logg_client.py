import socket, sl4a 

def logging():
    host = '193.157.210.105'
    port = 60002
    droid = sl4a.Android()
    s = socket.socket()
    s.connect((host,port))
    droid.webViewShow('Internal Storage/qpython/projects3/WebAppSample/logg.html')
    recv = droid.eventWait().result
    s.send('logg,{}'.format(recv).encode())
    reply = s.recv(1024).decode()
    droid.makeToast(reply)
    s.close()

if __name__=='__main__':
    logging()
