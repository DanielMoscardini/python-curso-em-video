"""
Faça um software que leia o comprimento do cateto oposto e do cateto adjacente de um traingulo retangulo,
e retorne a sua hipotenusa
"""
from math import pow, sqrt
CatAdj = float(input('Qual o valor do Cateto Adjacente: '))
CatOpo = float(input('Qual o valor do Cateto Oposto: '))
Hipotenusa = (pow(CatAdj,2) + pow(CatOpo,2))
ValorHipotenusa = sqrt(Hipotenusa)
print(f'Lado1: {CatOpo}, Lado2: {CatAdj}, Hipotenusa: {(int(ValorHipotenusa))}')
"""
from math import hypot
CatAdj = float(input('Qual o valor do Cateto Adjacente: '))
CatOpo = float(input('Qual o valor do Cateto Oposto: '))
ValorHipotenusa = hypot(CatAdj,CatOpo)
print(f'Lado1: {CatOpo}, Lado2: {CatAdj}, Hipotenusa: {(int(ValorHipotenusa))}')
"""