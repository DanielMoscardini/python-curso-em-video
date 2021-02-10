"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par().
A primeira função vai sortear 5 números e vai colocá-los dentro de uma lista,
e a segunda função vai mostrar a soma entre todos os valores PARES soteados pela função anterior.
"""
from random import randint
from time import sleep


def sorteia(lista):
	print(f'Sorteando 5 valores da lista: ', end='')
	for cont in range(0, 5):
		n = randint(1, 10)
		lista.append(n)
		print(f'{n} ', end='')
		sleep(0.3)
	print(f'Pronto!')


numeros = list()
sorteia(numeros)


def soma_par(lista):
	soma = 0
	for valor in lista:
		if valor % 2 == 0:
			soma += valor
	print(f'Somando os valores pares de {lista}, temos a soma {soma}')


soma_par(numeros)


def contador(i, f, p):
	"""
	-> Faz uma contagem e mostra na tela.
	:param i: Inicio da Contagem
	:param f: Fim da Contagem
	:param p: Passo da Contagem
	:return: Sem Retorno
	"""
	c = i
	while c <= f:
		print(f'{c} ', end='')
		c += p
	print(f'FIM')


help(contador)
