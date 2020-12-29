import socket
ip= input("enter ur ip adress")
port=90
sock=socket.socket()
try:
    sock.connect((ip,port))
    print("port is open")
except:
    print("port is closed")

