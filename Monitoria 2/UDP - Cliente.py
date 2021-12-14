import socket
from typing import ByteString

serverAddressPort = ('localhost', 28886)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
inputClient=""

while (inputClient != 'quit'):
    inputClient = input()
    msgFromClient = bytes(inputClient, 'utf-8') 

    UDPClientSocket.sendto(msgFromClient, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    print("Message from server: {}".format(msgFromServer[0].decode('utf-8')))
