import socket
import datetime as dt

localPort = 28886
bufferSize = 1024

#msgFromServer = bytes("Hello UDP client", 'utf-8')

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind(('localhost',localPort))

print("O servidor UDP está pronto")
#============================respostas padroes==========================
agora = dt.datetime.now();
agora1 = agora.strftime("%H:%M:%S")
agorastr =str(agora1)
horas = bytes(agorastr, 'utf-8')
ano = bytes("Segundo o calendário chinês, estamos no Ano do Boi.", 'utf-8')
xau = bytes("Adeus", 'utf-8')
#=========================================================================
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    #print("mensagem from cliente: {}".format(message,'utf-8'))
    #print("Endereço IP do cliente: {}".format(address))
    if(message == bytes("Que horas são?", 'utf-8')):
        UDPServerSocket.sendto(horas, address)
    elif (message == bytes("Em que ano estamos?", 'utf-8')):
        UDPServerSocket.sendto(ano, address)
    elif (message == bytes("Encerrar", 'utf-8')):
        UDPServerSocket.sendto(xau, address)
        UDPServerSocket.close()
    else:
        #UDPServerSocket.sendto(message, address)
        print("mensagem from cliente: {}".format(message,'utf-8'))

    #UDPServerSocket.sendto(msgFromServer, address)#enviar mensagem pro cliente