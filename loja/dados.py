from main1 import *
c1 = Cliente('victor', '119390929')


print(c1.get_nome(), 'e', c1.telefone)


conta = Conta(c1.get_nome(), 5555, 0)

print(conta.titular, f'Numero: {conta.numero}', f'seu saldo é {conta.get_saldo}')


conta.extrato()

conta.saque(50)
conta.extrato()
conta.deposito(100)
conta.extrato()
conta.saque(30)
conta.extrato()