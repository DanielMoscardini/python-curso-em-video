"""
Leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere
"""
cont = 0
pares = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} numero: '))
    if (num % 2 == 0):
        pares += num
        cont += 1
print(f'Voce informou {cont} numeros. a soma dos numeros pares eh: {pares}')
