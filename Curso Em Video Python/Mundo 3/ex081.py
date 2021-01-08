"""
Crie um prorama que vai ler vários números e colocar em uma lista. Depois disso mostre:
A) Quantos numeros foram digitados.
B) A lista de valores ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.
"""
cont = 0
lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    cont += 1
    if resp in 'N':
        break

if 5 in lista:
    print('5 está na lista')
else:
    print('5 não esta na lista')
lista.sort(reverse=True)
print(f'Lista em order decrescente: {lista}')
print(f'Total de valores digitados: {cont}')
print('Fim do programa')