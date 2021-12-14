import socket
import datetime as dt
import time

#                                                             #
#   Apenas enviando e recebendo mensagem, sem a parte do tempo#
#                                                             #
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))

s.listen(1)

conn, addr = s.accept()
print("Server connected with: {} {}".format(addr[0], addr[1]))

mensagem_alerta = bytes("Alerta: Esta conexão será encerrada em breve!", 'utf-8')
loopTempo = True

while 1: #uma Chaves resolveria todo problema de indentação
    
    #==========================timer==============================
    agora = dt.datetime.now(); #tempo inicial
    daqui_um_segundo = agora + dt.timedelta(seconds = 20); #adciona 20sec em tempo inicial

    agora2 = agora.strftime("%H:%M:%S") #retirando a data
    depois = daqui_um_segundo.strftime("%H:%M:%S")
    #=============================================================
    #primeira msg do cliente
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    #enviando resposta
    data = input()
    conn.sendall(bytes(data, 'utf-8'))

    while loopTempo:
        data = conn.recv(1024)
        if not data:
            break
        print(data)

        data = input()
        conn.sendall(bytes(data, 'utf-8'))
            

conn.close()