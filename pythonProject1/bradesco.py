import math

class esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def volume(self):
        vol = (4/3)*math.pi*(self.raio**3)
        return vol
    def area(self):
        ar = 4*math.pi*(self.raio**2)
        return ar



bola1 = esfera('vermelha', 4)
bola2 = esfera('verde', 7)

print(f'volume da bola1 é {bola1.volume():.2f}cm³')

print(f'area da bola2 é {bola2.area():.2f}cm²')

print(bola1.volume())
print(esfera.volume(bola1))