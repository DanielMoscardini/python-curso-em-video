"""
Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido.
"""
import random
aluno1 = str(input('Qual o nome do 1ºaluno: '))
aluno2 = str(input('Qual o nome do 2ºaluno: '))
aluno3 = str(input('Qual o nome do 3ºaluno: '))
aluno4 = str(input('Qual o nome do 4ºaluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f'Aluno escolhido: {escolhido}')
