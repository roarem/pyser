import socket

def Main():
    host = '37.191.195.168'
    port = 60002

    mySocket = socket.socket()
    mySocket.connect((host,port))
    
    command = input(" -> ")

    while command != 'q':
        mySocket.send(command.encode())
        data = mySocket.recv(1024).decode()

        print('Received from server: ' + data)

        command = input(" -> ")

    mySocket.close()

if __name__=='__main__':
    Main()
