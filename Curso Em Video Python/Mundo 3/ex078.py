"""
Faça um programa que leia 5 valores numericoes e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista.
"""

listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores: {listanum}')
print(f'O maior valor digitado foi: {max(listanum)} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi: {min(listanum)} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i}...', end='')
print()