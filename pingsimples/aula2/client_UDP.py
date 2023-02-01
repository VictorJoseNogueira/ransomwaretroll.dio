import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('criação de cliente bem sucedida')
host = 'localhost'
porta = 5433
mensagem = 'OLA: servidor!!!'
try:
    s.sendto(mensagem.encode(), (host, 5432))
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'cliente: ' + dados)
finally:
    print('Cliente: fechando conexão!')
    s.close()