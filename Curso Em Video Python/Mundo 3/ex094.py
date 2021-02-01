"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acime da média;
"""

nome = []
sexo = []
idade = []

while True:
	nome.append(str(input('Nome: ')))
	sexo.append(str(input('M/F :  ')))
	idade.append(int(input('Idade: ')))
	resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
	if resp in 'N':
		break
	elif resp not in 'S':
		print(f'ERRO! Responda apenas S ou N.')
		resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
		if resp in 'N':
			break

print(f'Nome: {nome}\n'
	  f'Sexo: {sexo}\n'
	  f'Idade: {idade}')
