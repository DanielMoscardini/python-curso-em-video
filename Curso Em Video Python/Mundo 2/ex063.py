"""
Leia um numero inteiro qualquer e mostra na tela os n primeiros elementos de uma sequência de fibonacci
Ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
fibonacci -> Xn = Xn-1 + Xn-2
n = Termo de n
"""
n = int(input('Quantos termpos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')