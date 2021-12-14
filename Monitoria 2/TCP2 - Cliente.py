import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 28877))
s.connect(('localhost', 50000))

msg = input()

while (msg != 'quit'):
    
    s.sendall(bytes(msg, 'utf-8'))
    data = s.recv(1024)
    print('received ' + repr(data))
    msg = input()



s.close()
    