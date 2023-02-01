import os
from time import sleep
x = 'x' * 60
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('verificando IP')
        print(x)
        os.system(f'ping -n 4 {ip}')
        print(x)
        sleep(3)