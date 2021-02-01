"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador_gols = []
soma = cont = 0
jogador = {}
jogador['nome'] = str(input(f'Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, partidas + 1):
	jogador_gols.append(int(input(f'Quantos gols na {c}º partida? ')))
	soma = sum(jogador_gols)

jogador['gols'] = jogador_gols
jogador['total'] = soma

# 1º print:
print('-=' * 30)
print(jogador)
print('-=' * 30)

# 2º print:
print('-=' * 30)
for k, v in jogador.items():
	print(f'O campo {k} tem valor {v}')
print('-=' * 30)

# 3º print:
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(jogador['gols']):
	print(f'	Na partida {i + 1}, fez {v} gols')
print(f'Foi um total de {soma} gols')
print('-=' * 30)
