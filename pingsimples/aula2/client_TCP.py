import socket
import sys

def main():
    #tentar conexão
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('erro, a conexão falhou')
        print(f'erro {e}')
        sys.exit()
    print('socket criado com sucesso ')

    host_alvo = str(input('\033[32m digite o host IP a ser Conectado:\033[m '))
    porta_alvo = input('digite a porta a ser conectada: ')

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print(f'cliente TCP criado com sucesso no host: {host_alvo} e na porta: {porta_alvo}')
        s.shutdown(2)
    except socket.error as er:
        print('\033[31mERRO: a conexão falhou\033[m')
        print(f'erro {er}')
        sys.exit()

if __name__ == '__main__':
    main()