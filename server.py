#!/bin/python3
import socket
serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

port = 1234

serversocket.bind(('192.168.43.189' , port))
serversocket.listen(3)
print("ready")
while True :
            print("Starting ")
            clientsocket,address = serversocket.accept()
            print("connection for has been established! %r: %s" %(address))
            message = "Thanks for connection"
            clientsocket.send(bytes (message,"utf-8"))
            clientsocket.close()
            
print("complete")
