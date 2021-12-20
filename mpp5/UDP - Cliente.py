#codigo configurado na maquina de weslley
import socket
from typing import ByteString
import threading
import time

#serverAddressPort = ('201.59.169.4', 50005) #colocar ip do servidor e porta, configurados no roteador-servidor (julio)
#serverAddressPort = ('45.166.51.58', 1317) #colocar ip do servidor e porta, configurados no roteador-servidor (pedro)
serverAddressPort = ('localhost', 50000) #colocar ip do servidor e porta, configurados no roteador-servidor (local)

bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def envia():
    global countmsg
    countmsg = 0
    inputClient=""
    while (inputClient != 'quit'):
        while True: 
            inputClient = input()
            msgFromClient = bytes(str(countmsg+1) +') '+inputClient, 'utf-8')
            UDPClientSocket.sendto(msgFromClient, serverAddressPort)
            countmsg = countmsg+1
            #---verificação de intervalo---
            intervalomsg = countmsg % 10
            #------------------------------
            if(intervalomsg == 0 and countmsg!=0):      
                print("intervalo de 10 segundos")
                time.sleep(10)
                if(countmsg==30):
                    break
def recebe():
    #UDPClientSocket.bind(('192.168.1.110', 34942)) #porta para receber mensagem do servidor
    UDPClientSocket.bind(('localhost', 50001)) #porta para receber mensagem do servidor
    countAck=0
    while True:
        msgServidor = UDPClientSocket.recvfrom(1024)
        print("Messagem do servidor: {}".format(msgServidor[0].decode('utf-8')))
        msgServidor = msgServidor[0].decode('utf-8')
        msgAck = msgServidor.find('ack')
        
        if(msgAck != -1):
            countAck = countAck + 1
        if(countmsg == 30):
            taxaPerda = (countmsg-countAck)/countmsg
            print('taxa de perda: ', taxaPerda)
            UDPClientSocket.close()

enviar = threading.Thread(target=envia)
receber = threading.Thread(target=recebe)

receber.start()
enviar.start()