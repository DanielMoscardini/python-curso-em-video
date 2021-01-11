"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
Obs: Os numeros do mesmo jogo não devem repetir e devem estar em ordem crescente
Ex:
Quantos jogos você quer que eu sorteie? 4
Jogo 1: [4, 8, 10, 20, 26, 38]
Jogo 2: [14, 20, 23, 35, 38, 47]
Jogo 3: [2, 11, 15, 24, 43, 48]
Jogo 4: [6, 26, 28, 30, 46]
"""
from random import sample
from time import sleep

jogos = list()
n = int(input('Quantos jogos?: '))
for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a[:])
    print(f'Jogo {c + 1}: {a}')
    sleep(0.5)
