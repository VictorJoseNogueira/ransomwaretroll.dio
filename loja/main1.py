class Cliente:
    def __init__(self, n, telefone):
        self._nome = n
        self.telefone = telefone

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome


class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self._saldo = saldo
        self.numero = numero
    @property
    def get_saldo(self):
        return self._saldo

    @get_saldo.setter
    def set_saldo(self, saldo):
        if saldo < 0:
            print('o saldo nao pode ser negativo')
        else:
            self._saldo = saldo

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print('saque realizado com sucesso')
        else:
            print('saldo insuficiente')


    def deposito(self, valor):
        self._saldo += valor

    def extrato(self):
        print(f'cliente: {self.titular}, seu saldo atual é de R$ {self._saldo:.2f}')


