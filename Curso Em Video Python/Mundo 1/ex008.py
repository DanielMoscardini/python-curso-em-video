"""
Faça um software que receba um valor em metros e converta para centimentros e milimetros
"""
valorMetros = float(input('Qual o valor em metros? '))
valorCentimentros = valorMetros * 100
valorMilimetros = valorMetros * 1000
print(f'Valor em: \nMetros: {valorMetros} \nCentimentros: {valorCentimentros:.0f} \nMilimetros: {valorMilimetros:.0f}')