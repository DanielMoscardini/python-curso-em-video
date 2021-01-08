"""
Leia um numero e mostre seu fatorial
Ex:
5! = 5 x 4 x 3 x 2 x 1 = 120
OBS: Usando o módulo
from math import factorial
numero = int(input('Digite um numero para calcular seu fatorial: '))
print(f'Fatorial de {numero} é {factorial(numero)}')
"""
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {c}! = ', end='')
while (c > 0):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print(f'Fatorial de {n} é {f}')






