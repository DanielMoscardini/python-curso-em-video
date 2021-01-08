"""
Faça um software que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e RS0,15 por km rodado.
"""
DiasAlugados = int(input('Quantos dias você ficou com o carro? '))
QuilometrosRodados = float(input('Quantos Quilometros você andou?'))
CustoTotal = (DiasAlugados * 60) + (QuilometrosRodados * 0.15)
print(f'Você ficou o carro por {DiasAlugados}, e andou {QuilometrosRodados}, portanto, deve pagar {CustoTotal}')
