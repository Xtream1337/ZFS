import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print(host)
#name = input(str("Username : "))
s.listen(1)

print("Waiting for connection 2")

#conns = []
#conns.append(conn1)
conn, addr = s.accept()
print ("1 recieved connection")
conn.send("Welcome2".encode())
print("Waiting  for connection 1")
conn1, addr1 = s.accept()
print ("2 recieved connection")
conn1.send("Welcome2".encode())
##s_name = conn.recv(1024)
##s_name = s_name.decode()
##print(s_name, "Has connected to chat room")
##conn.send(name.encode())

while 1:
    message = input(str("Enter message : "))
    message = message.encode()
    conn.send(message)
    conn1.send(message)
    print("Sent")
    recv_message = conn.recv(1024)
    print("client : ", recv_message.decode())
    conn1.send(recv_message)
    recv_message = conn1.recv(1024)
    print("client : ", recv_message.decode())
    conn.send(recv_message)
##    message = message.decode()
##    print(name, " : ", message)