class tv:
    def __init__(self, fabricante, modelo):
            self.fabricante = fabricante
            self.modelo = modelo
            self.canal_atual = None
            self.lista_de_canais = []
            self.volume = 20

    def aumentar_volume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuir_volume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def sintonizar(self, canal):
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)

    def troca(self,canal):
        if canal in self.lista_de_canais:
            self.canal_atual = canal
        else:
            pergunte = str(input('deseja sintonizar o canal ? \naperte S para sim ou qualquer outra tecla para nao(menos o botao power): ')).strip()
            if pergunte in 'sS':
                self.sintonizar(canal)
                print('sintonizado com exito')
            else:
                print('ok ')





tvdoquarto = tv('philip', 'semptoshiba2000')
print(tvdoquarto.volume)
tvdoquarto.diminuir_volume(5)
print(tvdoquarto.volume)
tvdoquarto.aumentar_volume(100)
print(tvdoquarto.volume)
print(tvdoquarto.lista_de_canais)
tvdoquarto.sintonizar('globo')
tvdoquarto.sintonizar('sbp')
print(tvdoquarto.lista_de_canais)
tvdoquarto.troca('hbo')
print(tvdoquarto.lista_de_canais)