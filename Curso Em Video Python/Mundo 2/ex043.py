"""
Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
-abaixo de 18.5: ABAIXO DO PESO
-entre 18.5 e 25: PESO IDEAL
-25 até 30: SOBREPESO
-30 até 40: OBESIDADE
-acima de 40: OBESIDADE MORBIDA
"""
from math import pow
peso = float(input('Digite o peso(Kg): '))
altura = float(input('Digite a altura(M): '))
imc = peso / (pow(altura, 2))
if (imc < 18.5) :
    print(f'IMC: {imc} \nABAIXO DO PESO')
elif (18.5 <= imc < 25) :
    print(f'IMC: {imc} \nPESO IDEAL')
elif (25 <= imc < 30):
    print(f'IMC: {imc} \nSOBREPESO')
elif (30 <= imc < 40):
    print(f'IMC: {imc} \nOBESIDADE')
else :
    print(f'IMC: {imc} \nOBESIDADE MORBIDA')