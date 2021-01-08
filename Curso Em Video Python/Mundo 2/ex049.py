"""
Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, utilizando o laco FOR
"""
num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    #print(c)
    print(f'{num} x {c} = {num * c}')