"""
Faça um software que leia as duas notas de um aluno e calcule sua média
"""
nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
media = (nota1 + nota2) / 2
print(f'A media de {nota1} e {nota2} é {media:.2f}')