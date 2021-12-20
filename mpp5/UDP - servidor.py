#julio
import socket
import datetime as dt

localPort = 55555 #porta
portEnvio = 1080
bufferSize = 1024
#endPortaEnvio = ('45.6.136.180',1080) #ip e porta do roteador cliente
endPortaEnvio = ('localhost',50001) #ip e porta do roteador cliente
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#UDPServerSocket.bind(('192.168.1.7',localPort)) #ip local e porta para receber dados
UDPServerSocket.bind(('localhost',50000)) #ip local e porta para receber dados(local)
print("O servidor UDP está pronto")

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    msg = bytesAddressPair[0]
    endPorta = bytesAddressPair[1]

    msgdecode = msg.decode('UTF-8')
    recebido = msgdecode.split(')')    
    msgFormatada = bytes("ack: " + recebido[0], 'utf-8')
    UDPServerSocket.sendto(msgFormatada, endPortaEnvio)