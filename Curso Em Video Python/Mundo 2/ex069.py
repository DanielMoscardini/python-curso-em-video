"""
Leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados
C) quantas mulheres tem menos de 20 anos
"""
pessoas = 0
homens = maiorDeDezoito = mulheresMenosVinte = 0
escolha = 'S'
while escolha in 'S':
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]
    pessoas += 1
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if idade >= 18:
        maiorDeDezoito += 1

    if sexo in 'M':
        homens += 1

    if sexo in 'F' and idade < 20:
        mulheresMenosVinte += 1

print(f'Foram cadastradas {pessoas} pessoas, onde \n'
      f'{maiorDeDezoito} são maioritarios\n'
      f'{homens} são homens\n'
      f'{mulheresMenosVinte} são mulheres menores de 20 anos')
