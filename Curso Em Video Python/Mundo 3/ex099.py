"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(*num):
	cont = maior = 0
	print('-' * 30)
	print('\nAnalisando os valores passados...')
	for valor in num:
		print(f'{valor} ', end='')
		sleep(.3)
		if cont == 0:
			maior = valor
		else:
			if valor > maior:
				maior = valor
		cont += 1
	print(f'Foram informados {cont} ao todos.')
	print(f'O maior valor informado foi {maior}')


maior(4, 9, 8, 1)
maior(78, 951, 0)
maior(1, 9)
maior(8, 6, 45, 6, 854)
maior(7, 9, 58)
