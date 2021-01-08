"""
Mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o numero solicitado for negativo
"""
while True:
    num = int(input('Digite um numero: '))
    if (num < 0):
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('FIM')
