"""
Reafaça o ex051, leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos de uma progressão, porem agora usando a estrutura while
"""
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = primeiroTermo
cont = 1
while (cont <= 10):
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')
