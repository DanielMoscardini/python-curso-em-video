"""
Faça um software que pergunte o salario de um funcionário e calcule o valor do seu aumento:
-Para salário maiores ou iguais a R$1250,00, calcule um aumento de 10%
-Para salarios inferiores a R$1250,00, o aumento é de 15%
"""
salario = float(input('Digite seu salário: '))
if (salario >= 1250):
    print(f'Salario Atual: {salario}    \nSalario Com Aumento de 10%: {salario + (salario * 10 / 100)}')
else :
    print(f'Salario Atual: {salario}    \nSalario com Aumento de 15%: {salario + (salario * 15 / 100)}')