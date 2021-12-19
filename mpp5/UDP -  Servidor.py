#codigo configurado na maquina de julio
import socket
import datetime as dt

localPort = 55555 #porta
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind(('192.168.1.7',localPort))
#UDPServerSocket.bind(('192.168.1.7',localPort))#ip da maquina em ('localhost')

print("O servidor UDP está pronto")
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]

print('Servidor conectado em: ', address)
while(True):
    #============================respostas padroes==========================
    agora = dt.datetime.now()
    agora1 = agora.strftime("%H:%M:%S")
    agorastr =str(agora1)
    horas = bytes(agorastr, 'utf-8')
    ano = bytes("Segundo o calendário chinês, estamos no Ano do Boi.", 'utf-8')
    xau = bytes("Adeus", 'utf-8')
    #=========================================================================

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print('Servidor conectado em: ', address)

    if(message == bytes("Que horas são?", 'utf-8')):
        UDPServerSocket.sendto(horas, address)
    elif (message == bytes("Em que ano estamos?", 'utf-8')):
        UDPServerSocket.sendto(ano, address)
    elif (message == bytes("Encerrar", 'utf-8')):
        UDPServerSocket.sendto(xau, address)
        UDPServerSocket.close()
    else:
        print("mensagem from cliente: {}".format(message,'utf-8'))