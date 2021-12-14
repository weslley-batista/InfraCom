import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.bind(('0.0.0.0', 31415)) #sem função APARENTEMENTE
socket_client.connect(('localhost', 50000))#conectado a [1] pela porta [2]

msg = input()

while msg != 'quit':
    socket_client.sendall(bytes(msg,'utf-8'))
    data = socket_client.recv(1024)
    print('received ' + repr(data))
    msg = input()

socket_client.close()