import socket, sl4a 

def logging():
    host = '193.157.210.105'
    port = 60002
    droid = sl4a.Android()
    s = socket.socket()
    s.connect((host,port))
    droid.webViewShow('file:///storage/emulated/0/qpython/mine/logg.html')
    while True:
        recv = droid.eventWait().result
        if recv['name']=='message':
            s.send('logg,{}'.format(recv).encode())
            reply = s.recv(1024).decode()
            break
        else:
            continue

    droid.makeToast(reply)
    s.close()
if __name__=='__main__':
    logging()
