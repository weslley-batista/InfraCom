import socket

localhost = 200001
portConnection = 50005 #porta que será usada na conexão P2P

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind(('localhost', 55555))

while 1:
    conexoesCliente =  [] #pilha para guardar conexoes
    while 1:
        
        for i  in range(2): #[0,1]
            addressPair = socket_server.recvfrom(1024)
            message = addressPair[0]
            address = addressPair[1]
            
            conexoesCliente.append(address)
            print("Cliente conectado (", address[0],address[1], ")")
        
        #separando endereço e enviando mensagem de conexão aos clientes
        cliente1 = conexoesCliente.pop()
        cliente1_addr, cliente1_port = cliente1
        socket_server.sendto(b'Dois usuarios conectados', cliente1)
        
        cliente2 = conexoesCliente.pop()
        cliente2_addr, cliente2_port = cliente2
        socket_server.sendto(b'Dois usuarios conectados', cliente2)

        #informações para servidores contrarios
        socket_server.sendto('{} {} {}'.format(cliente1_addr, cliente1_port, portConnection).encode(),cliente2)

        socket_server.sendto('{} {} {}'.format(cliente2_addr, cliente2_port, portConnection).encode(),cliente1)
