import socket
import sys #funcionalidades do sistema
import threading
import time

#ipCliente2 = ('147.182.184.215', 55555)
ipCliente2 = ('localhost', 55555)
portafonte = 50002

socket_cliente2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente2.bind(('localhost', portafonte))
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
socket_cliente2.sendto(b'0', (ip, sourcePort))

#listener colocar data e nome no print
def listen():
    while 1:
        #dataHora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        msgClient = socket_cliente2.recv(1024)
        print('cliente 1: {}\n'.format(msgClient.decode()))
        

listener = threading.Thread(target=listen)
listener.start()

#send
def send():
    while 1:
        dataHora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        dataHora = str(dataHora)
        msgSend = input(dataHora +' > ')
        socket_cliente2.sendto(msgSend.encode(), (ip, sourcePort))

enviando = threading.Thread(target=send)
enviando.start()