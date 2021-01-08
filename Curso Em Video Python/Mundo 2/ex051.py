"""
Leia o primeiro termo e a razao de uma PA. No final mostre os 10 primeiros termos dessa progressao
"""
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiroTermo + (10 - 1) * razao #forma pra descobrir enezimo termo de uma PA
for c in range(primeiroTermo, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('FIM')