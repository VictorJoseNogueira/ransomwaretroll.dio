import random, string

tamanho = 16
pergunta = input()
chars = string.ascii_letters + string.digits + '!@#$%&*-_=+?/|'

rnd = random.SystemRandom() #os.urandom

print(f''.join(rnd.choice(chars) for i in range(tamanho)))