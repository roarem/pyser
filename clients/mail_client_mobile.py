import socket, sl4a, time

class Mail:
    def __call__(self):
        title = 'Mail'
        host = '37.191.195.168'
        port = 60002
        droid = sl4a.Android()
        s = socket.socket()
        s.connect((host,port))
        s.send('mail'.encode())
        message = s.recv(1024).decode() 
        droid.dialogCreateSpinnerProgress(title,message)
        droid.dialogShow() 
        time.sleep(2)
        droid.dialogDismiss()
        s.close()

if __name__=='__main__':
    test = Mail()
    test()
