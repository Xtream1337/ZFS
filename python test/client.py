import time
import socket
import sys

print("Welcome to chat")
time.sleep(1)

s = socket.socket()
print("")
host = input(str("Server adress : "))
name = input(str("Username:"))
port = 8080
print("trying to connect  to ", host, " at port", port)
time.sleep(1)
s.connect((host, port))
print("connected")

##connection done###

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "Has joined the chat")

while 1:
    message = s.recv(1024)
    message = message.decode()
    print(name, " : ", message)
    message = input(str("Enter message : "))
    s.send(message.encode())
    print("Sent")

##chat##