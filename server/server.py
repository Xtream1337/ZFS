import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print(host)
#name = input(str("Username : "))
s.listen(1)

print("Waiting for 4 connection ")

N=4
conns = []
for i in range(N):

    conn, addr = s.accept()
    conns.append(conn)
    print("WELCOME  "+str(i))
    conn.send("Welcome4".encode())

##s_name = conn.recv(1024)
##s_name = s_name.decode()
##print(s_name, "Has connected to chat room")
##conn.send(name.encode())

while 1:
    message = input(str("Enter message : "))
    message = message.encode()
    for conn in conns:
        conn.send(message)
        print("Sent")
        
    for conn in conns:
        recv_message = conn.recv(1024)
        print("client", recv_message.decode())
        #recv_message["timestamp"] = datetime.now()
        for other in conns:
            if other != conn:
                other.send(recv_message)

    
##    message = message.decode()
##    print(name, " : ", message)