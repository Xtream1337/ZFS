import time
import socket
import sys

print("Welcome to chat")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print(host)
name = input(str("Username : "))

s.listen(1)

print("Waiting for connection")

conn, addr = s.accept()
print ("recieved connection")


#connection done###

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "Has connected to chat room")
conn.send(name.encode())

while 1:
    message = input(str("Enter message : "))
    conn.send(message.encode())
    print("Sent")