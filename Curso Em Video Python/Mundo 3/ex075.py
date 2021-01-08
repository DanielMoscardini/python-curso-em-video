"""
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os numeros pares
"""

# Criando uma tupla a partir de um Input:
num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))

print(f'A tupla ficou assim: {num}')
# count vai dizer quantas vezes algum valor apareceu na tupla
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    # index retorna a posição em que algum valor está na tupla
    print(f'O primeiro valor 3 foi encontrado na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
