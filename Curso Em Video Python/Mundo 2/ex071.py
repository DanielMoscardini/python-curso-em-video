"""
Simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual sera o valor a ser sacado(valor inteiro)
e o programa vai informar quantas cedulas de cada valor serão entregues.
OBS: Considere que o caixa possui cedulas de: R$50, R$20, R$10 e R$1
"""

valor = int(input('Que valor você quer sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} celulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
