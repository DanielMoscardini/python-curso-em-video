"""
Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso crie duas listas extras que vão
conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Valores na lista: {lista}'
      f'Pares: {pares}\n'
      f'Impares: {impares}')