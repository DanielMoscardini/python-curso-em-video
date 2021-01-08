"""
Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
-EQUILATERO: todos os lados iguais
-ISOSCELES: dois lados iguais
-ESCALENO: todos os lados diferentes
"""
r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))
if r1 < r2 + r3 and r3 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triangulos')
    if (r1 == r2 and r2 == r3):
        print(f'Triangulo Equilatero')
    elif (r1 != r2 and r2 != r3 and r1 != r3):
        print(f'Triangulo Escaleno')
    else:
        (print(f'Triangulo Isosceles'))
else :
    print('Os seguimentos acima não podem formar triangulos')
