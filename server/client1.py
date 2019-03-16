import socket

s = socket.socket()
port = 8080
host=socket.gethostname()
#print(host, port)
s.connect((host, port))
print("connected")

##s.send(name.encode())
message = s.recv(1024)
message = message.decode()
print("Server message : ", message)

while 1:
    message = s.recv(1024)
    message = message.decode()
    print("Server: ", message)
    message = s.recv(1024)
    message = message.decode()
    print("Server: ", message)
    new_message = input(str("Enter message : "))
    new_message = new_message.encode()
    s.send(new_message)
    print("Sent")

##chat##