"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar de 80Km/h, mostre uma mensagem, dizendo
que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidadeAtual = float(input('Qual sua velocidade atual? '))
if (velocidadeAtual <= 80) :
    print(f'Sua velocidade atual é de: {velocidadeAtual}Km/h, tenha um bom dia')
else :
    print(f'Sua velocidade atual é de: {velocidadeAtual}Km/h, você vai ser MUTADO!!!')
    multa = (velocidadeAtual - 80) * 7
    print(f'Sua multa é de: {multa}R$')