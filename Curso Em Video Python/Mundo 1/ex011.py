"""
Faça um software que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tintas necessária
sabendo que a cada lintro de tinta, é pintado 2m²
"""
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a larguta da parede: '))
area = altura * largura
litros = area / 2
print(f'Tamanho da área da parede: {area}m², e vai precisar de {litros} litros de tinta')