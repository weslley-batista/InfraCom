#codigo configurado na maquina de weslley
import socket
from typing import ByteString
import threading

#serverAddressPort = ('201.59.169.4', 50005) #colocar ip do servidor e porta, configurados no roteador-servidor (julio)
serverAddressPort = ('45.166.51.58', 1317) #colocar ip do servidor e porta, configurados no roteador-servidor (pedro)

bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def envia():
    countmsg = 0
    inputClient=""
    while (inputClient != 'quit'):
        while True:
            countmsg = countmsg+1

            inputClient = input()
            msgFromClient = bytes(str(countmsg) +') '+inputClient, 'utf-8') #contador + input
            UDPClientSocket.sendto(msgFromClient, serverAddressPort)

def recebe():
    UDPClientSocket.bind(('192.168.1.110', 34942)) #porta para receber mensagem do servidor
    while True:
        msgServidor = UDPClientSocket.recvfrom(1024)
        print("Messagem do servidor: {}".format(msgServidor[0].decode('utf-8')))

enviar = threading.Thread(target=envia)
receber = threading.Thread(target=recebe)

receber.start()
enviar.start()