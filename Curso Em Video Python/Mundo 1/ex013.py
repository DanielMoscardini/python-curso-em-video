"""
Faça um software que leia o salário de um funcionário e retorne seu novo salário com 15% de aumento
"""
SalarioAtual = float(input('Digite seu salário atual: '))
Aumento = (SalarioAtual * 15 / 100) #15%
NovoSalario = SalarioAtual + (Aumento)
print(f'Salario ORIGINAL: {SalarioAtual}, Salario Novo: {NovoSalario}')