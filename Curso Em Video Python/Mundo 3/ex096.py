"""
Faça um programa que tenha uma função chamada area(), que calcule as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno
"""


def area (l, c):
	a = l * c
	print(f'A área de um terreno {l} * {c} é de {a}m² ')
	
	

print(f'Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
