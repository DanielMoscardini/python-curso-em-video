"""
O professor do exercício anterior, quer sortear a ordem de apresentação de trabalho dos alunos. Faça um software que
leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
import random
aluno1 = str(input('Qual o nome do 1ºaluno: '))
aluno2 = str(input('Qual o nome do 2ºaluno: '))
aluno3 = str(input('Qual o nome do 3ºaluno: '))
aluno4 = str(input('Qual o nome do 4ºaluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem de apresentação sera:'
      f'\n{lista}')