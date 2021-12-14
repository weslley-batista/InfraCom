import socket
import sys #funcionalidades do sistema
import threading

#ipCliente2 = ('147.182.184.215', 55555)
ipCliente2 = ('localhost', 55555)
portafonte = 50002

socket_cliente2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente2.bind(('0.0.0.0', portafonte))
socket_cliente2.sendto(b'0', ipCliente2)

while 1:
    data = socket_cliente2.recv(1024).decode()
    print(data)
    break

data = socket_cliente2.recv(1024).decode()
ip, sourcePort, destPort = data.split(' ')
sourcePort = int(sourcePort)
destPort = int(destPort)

print('Dados do outro cliente')
print('Ip:              {}'.format(ip))
print('Porta de origem: {}'.format(sourcePort))
print('Porta destino:   {}\n'.format(destPort))

#p2p
socket_cliente2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente2.bind(('0.0.0.0', sourcePort))
socket_cliente2.sendto(b'0', (ip, destPort))

#thread listen
def listen():
    socket_cliente2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_cliente2.bind(('localhost', sourcePort))

    while True:
        data = socket_cliente2.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True);
listener.start()

#socket pra envio
socket_cliente2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente2.bind(('localhost', destPort))

while 1:
    msg = input('> ')
    socket_cliente2.sendto(msg.encode(), (ip, sourcePort))