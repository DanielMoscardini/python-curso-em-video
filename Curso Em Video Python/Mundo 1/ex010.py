"""
Faça um software que leia uma quantidade de dinheiro em reais e devolva em dolar:
Considere US$1,00 = R$3,27
"""
dinheiro = float(input('Quanto você tem de dinheiro? '))
dolar = 3.27
ConverteEmDolar = (dinheiro / dolar)
print(f'{dinheiro} reais é igual à: {ConverteEmDolar:.2f} dolares')