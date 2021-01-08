"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
matriz: 0, 1, 2 x 0, 1, 2 (um valor para cada posição [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2])
No final, mostre a matriz na tela, com a formatação correta
Ex:
[1] [2] [3]
[4] [5] [6]
[7] [8] [9]
"""
matriz = [[0, 0, 0], [0, 0, 0, ], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='') #formata em 5 casa decimais, centralizadas
    print() #Identação para quebrar uma linha assim que completar o for