"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
"""
num = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o número da {c + 1}º posição: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'-=' * 30)
num[0].sort()
num[0].sort()
print(f'Todos os valores pares: {num[0]}')
print(f'Todos os valores impares: {num[1]}')