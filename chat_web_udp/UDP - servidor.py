import socket
import datetime as dt

localPort = 55555 #porta
portEnvio = 1080
bufferSize = 1024
endPortaEnvio = ('45.6.136.180',1080) #ip e porta do roteador cliente (weslley)
#endPortaEnvio = ('localhost',50001) #ip e porta do roteador cliente (local)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#UDPServerSocket.bind(('192.168.1.7',localPort)) #ip local e porta para receber dados (maquina)
#UDPServerSocket.bind(('localhost',50000)) #ip local e porta para receber dados(local)
UDPServerSocket.bind(('192.168.1.110',34942)) #ip local e porta para(weslley)
print("O servidor UDP está pronto")

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    msg = bytesAddressPair[0]
    endPorta = bytesAddressPair[1]

    msgdecode = msg.decode('UTF-8')
    print(msgdecode)
    recebido = msgdecode.split(' ')
    msgFormatada = bytes("ack: " + recebido[0], 'utf-8')
    UDPServerSocket.sendto(msgFormatada, endPorta)