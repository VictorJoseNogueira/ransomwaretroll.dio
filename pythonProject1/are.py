import time
import os

class cronometro:
    def __init__(self, s=0, min=0, h=0):
        self.segundos = s
        self.minutos = min
        self.horas = h

    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.horas += 1

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)


cronometro1 = cronometro()
cronometro1.start()
