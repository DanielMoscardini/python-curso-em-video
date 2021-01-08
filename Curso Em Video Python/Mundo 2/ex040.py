"""
Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com
a media atingida:
-media abaixo de 5.0: REPROVADO
-media entre 5.0 e 6.9: RECUPERAÇÃO
-media 7.0 ou superior: APROVADO
"""
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if (media < 5.0) :
    print(f'Media: {media} -> REPROVADO')
elif (6.9 > media >= 5.0) :
    print(f'Media: {media} -> RECUPERACAO')
else :
    print(f'Media: {media} -> APROVADO')
