"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter  # Função pra pegar item do dicionário

jogo = {
	'jogador1': randint(1, 6),
	'jogador2': randint(1, 6),
	'jogador3': randint(1, 6),
	'jogador4': randint(1, 6)
}

ranking = []

print(f'Valores sorteados: ')
for k, v in jogo.items():
	print(f'{k} tirou {v} no dados.')
	sleep(.5)

print(f'\nPosições: \n'
	  f'')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # ordenar valor do dicionario
for i, v in enumerate(ranking):
	print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
	sleep(.5)
