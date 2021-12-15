import socket
import sys #funcionalidades do sistema
import threading
import time

ipCliente1 = ('localhost', 55555)
#portafonte = 50001
portafonte = 64001

socket_cliente1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente1.bind(('localhost', portafonte))
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
data, adress = socket_cliente1.recvfrom(128)
msgCheck = "mensagem recebida com sucesso"

#listener colocar data e nome no print
def listen():
    while 1:
        dataHora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        dataHora = str(dataHora)

        msgClient = socket_cliente1.recv(1024)
        print(dataHora + 'cliente 2: {}\n'.format(msgClient.decode()))

        if msgClient!=b'mensagem recebida com sucesso no cliente 2':
            socket_cliente1.sendto(b'mensagem recebida com sucesso no cliente 1', (ip, sourcePort))
            

listener = threading.Thread(target=listen)
listener.start()

#send
def send():
    countMsg = 0
    while 1:
        countMsg = countMsg + 1
        dataHora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        dataHora = str(dataHora)

        msgSend = input('{}'.format(countMsg) + ' '+ dataHora +' > ')
        socket_cliente1.sendto(msgSend.encode(), (ip, sourcePort))

enviando = threading.Thread(target=send)
enviando.start()