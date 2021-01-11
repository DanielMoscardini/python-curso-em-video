"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha

Ex(mesma matriz do ex passado):
A soma dos valores pares é 20
A soma dos valores da terceira coluna é 18
O maior valor da segunda linha é 6
"""
matriz = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]
pares = maior = Somacoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:  # Filtrando valores pares da matriz
            pares += matriz[l][c]  # Somando valores pares da matriz
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {pares}')
for l in range(0, 3):
    Somacoluna += matriz[l][2]  # A 3 coluna se encontra na posição 2, em linhas variadas
print(f'A soma dos valores da terceira coluna é: {Somacoluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
