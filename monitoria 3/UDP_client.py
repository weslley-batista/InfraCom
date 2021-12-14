import socket
import sys #funcionalidades do sistema
import threading

ipCliente1 = ('localhost', 55555)
portafonte = 50001

socket_cliente1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente1.bind(('0.0.0.0', portafonte))
socket_cliente1.sendto(b'0', ipCliente1)

while 1:
    data = socket_cliente1.recv(1024).decode()
    if data:
        print(data)
        break

data = socket_cliente1.recv(1024).decode()
ip, sourcePort, destPort = data.split(' ')
sourcePort = int(sourcePort)
destPort = int(destPort)

print('Dados do outro cliente')
print('Ip:              {}'.format(ip))
print('Porta de origem: {}'.format(sourcePort))
print('Porta destino:   {}\n'.format(destPort))

#p2p
socket_cliente1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente1.bind(('localhost', sourcePort))
socket_cliente1.sendto(b'0', (ip, destPort))

#thread listen
def listen():
    socket_cliente1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_cliente1.bind(('localhost', sourcePort))

    while True:
        data = socket_cliente1.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True);
listener.start()

#socket pra envio
socket_cliente1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente1.bind(('0.0.0.0', destPort))

while 1:
    msg = input('> ')
    socket_cliente1.sendto(msg.encode(), (ip, sourcePort))