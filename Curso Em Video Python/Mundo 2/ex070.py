"""
Leia o nome e preço de varios produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
A) qual é o total gasto na compra
B) quantos produtos custam mais de R$1000
C) qual é o nome do produto mais barato
"""
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa!')
print(f'O valor total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de mil reais')
print(f'O produto mais barato foi {barato} custa: {menor}')