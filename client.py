#!/bin/python3
import socket
clientsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

port = 1234
clientsocket.connect(('192.168.43.189' , port))
message  = clientsocket.recv(1024)
clientsocket.close()
print(message.decode("utf-8"))
