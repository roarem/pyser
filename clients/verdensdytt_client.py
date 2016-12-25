import socket, sl4a

def verdytt_add():
    host = '193.157.210.105'
    port = 60002
    droid = sl4a.Android()
    s = socket.socket()
    s.connect((host,port))
    number = droid.dialogGetInput("Verdensdytter","Antall verdensdytt","")
    s.send('dytt,{}'.format(number.result).encode())
    reply = s.recv(1024).decode()
    droid.makeToast(reply)
    s.close()

if __name__=='__main__':
    verdytt_add()
