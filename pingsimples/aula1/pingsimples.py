import os
ip_ou_host = str(input('digite o ip ou host a ser verificado: '))

os.system(f'ping -n 6 {ip_ou_host}')