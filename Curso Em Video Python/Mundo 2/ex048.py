"""
Calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 ate 500.
"""
cont = 0 #contador
soma = 0 #acumulador
for c in range (1, 501, 2):
    if (c % 3 == 0):
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados eh: {soma}')
