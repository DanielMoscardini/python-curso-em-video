"""
Faça um programa que leia o nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma listagem com as pessoas mais leves;
Lembrando que se os maiores/menores pesos forem iguais, deve-se mostrar todos os maiores e todos os menores, mesmo que iguais
"""
temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()

    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break

print(f'Ao todo você cadastrou {len(principal)} pessoas' )
print(f'O maior peso foi de {maior}Kg',end=' ' )
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}',end=' ' )
print(f'\nO menor peso foi de {menor}Kg',end=' ')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}',end=' ')