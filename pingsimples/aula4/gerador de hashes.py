import hashlib
from time import sleep

string = input('digite  o texto a ser convertido: ')

while True:
    menu = int(input('''### MENU escolha um tipo de hash ###
        #1: MD5
        #2: SHA1
        #3: SHA256
        #4: SHA512
        #5: TODOS
        digite o numero desejado: 
        '''))
    if menu in [1, 2, 3, 4, 5]:
        print('tudo certo')
        sleep(1)
        break
    else:
        print('\033[31mpor favor digite um numero valido!\033[m')
        sleep(1)
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print(f'o hash MD5 gerado a partir da {string} é: {resultado.hexdigest()}')

elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print(f'o hash SHA1 gerado a partir da {string} é: {resultado.hexdigest()}')
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print(f'o hash SHA256 gerado a partir da {string} é: {resultado.hexdigest()}')
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print(f'o hash SHA512 gerado a partir da {string} é: {resultado.hexdigest()}')
elif menu == 5:
    resultado1 = hashlib.md5(string.encode('utf-8'))
    resultado2 = hashlib.sha1(string.encode('utf-8'))
    resultado3 = hashlib.sha256(string.encode('utf-8'))
    resultado4 = hashlib.sha512(string.encode('utf-8'))
    print(f''' AS hash geradas a partir da string {string} sao:
    HASH MD5: {resultado1.hexdigest()}
    HASH SHA1: {resultado2.hexdigest()}
    HASH SHA256: {resultado3.hexdigest()}
    HASH SHA512: {resultado4.hexdigest()} 
    ''')
else:
    print('\033[31mERRO!!! tente novamente!!!\033[m')