import socket

socket_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket tipo TCP
socket_sever.bind(('localhost', 50000)) #esta ouvindo a porta 50000
socket_sever.listen(2) #numero maximo de requisições

conn, addr = socket_sever.accept()
print("Server connected with: {} {}".format(addr[0]), addr[1])

while 1: 
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    

conn.close()