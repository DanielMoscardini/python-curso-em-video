"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não criar um triangulo.
"""
r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))
if r1 < r2 + r3 and r3 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triangulos')
else :
    print('Os seguimentos acima não podem formar triangulos')