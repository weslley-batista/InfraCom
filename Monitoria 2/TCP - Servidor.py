import socket
import time
from typing import Counter
import datetime as dt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))

s.listen(1)

while 1: #loop de reconect
    
    conn, addr = s.accept()
    print("Server connected with: {} {}".format(addr[0], addr[1]))

    #==========================timer==============================
    agora = dt.datetime.now(); #tempo inicial
    daqui_um_segundo = agora + dt.timedelta(seconds = 20); #adciona 20sec em tempo inicial

    agora2 = agora.strftime("%H:%M:%S") #retirando a data
    depois = daqui_um_segundo.strftime("%H:%M:%S")
    #=============================================================

    while agora2!=depois: #loop de tempo maximo
        data = conn.recv(1024)
        if not data:
            break
        print(data) #print de mensagens enviadas do cliente no console servidor

        #atualiza tempo de conexao
        agora = dt.datetime.now();
        agora2 = agora.strftime("%H:%M:%S")

    conn.close()
    print ("conexao encerrada")