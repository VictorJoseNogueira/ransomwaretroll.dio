valor = float(input('digite o valor: '))
porcentagem = int(input('digite a %: '))
descacresc = str(input('o valor esta aumentando (+) ou diminuindo (-): '))
if descacresc == '+':
    conta = valor * (1+(porcentagem/100))
    print(conta)
elif descacresc == '-':
    conta = valor * (1-(porcentagem/100))
    print(conta)
