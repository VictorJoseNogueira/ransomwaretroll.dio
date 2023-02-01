import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('socked criado com sucesso')

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = '\n SERVIDOR: ola Victor'

while 1:
    dados, ender = s.recvfrom(4096)
    if dados:
        print('servidor enviando mensagem')
        s.sendto(dados + (mensagem.encode()), ender)

