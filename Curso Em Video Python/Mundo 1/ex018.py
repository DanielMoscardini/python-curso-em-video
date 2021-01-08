"""
Faça um software que leia um angulo qualquer e retorne seu Seno, Cosseno e Tangente do mesmo
"""
from math import sin, cos, tan, radians
Angulo = float(input('Digite o angulo: '))
Seno = sin(radians(Angulo))
Cosseno = cos(radians(Angulo))
Tangente = tan(radians(Angulo))
print(f'Angulo: {Angulo}º\n'
      f'Seno: {Seno:.2f}º\n'
      f'Cosseno: {Cosseno:.2f}º\n'
      f'Tangente: {Tangente:.2f}º')