"""
Faça um software que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
ex: 6.127 => 6
"""
from math import trunc
numero = float(input('Digite o numero: '))
print (f'Numero digitado: {numero}, parte inteira do numero: {int(numero)}')
print (f'Numero digitado: {numero}, parte inteira do numero: {trunc(numero)}')