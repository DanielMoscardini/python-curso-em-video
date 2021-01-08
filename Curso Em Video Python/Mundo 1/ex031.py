"""
Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
para viagem até 200Km, e R$0,45 para viagens mais longas.
"""
distancia = float(input('Qual a distancia da sua viagem? '))
if (distancia < 200):
    ateDuzentos = (distancia * 0.50)
    print(f'Sua viagem foi de {distancia}Km, e seu custo é de {ateDuzentos}')
else :
    maiorDuzentos = (distancia * 0.45)
    print(f'Sua viagem foi de {distancia}Km, e seu custo é de {maiorDuzentos}')
"""
OU:
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
Codigo mais enxuto
"""