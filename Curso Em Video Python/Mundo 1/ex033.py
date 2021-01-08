"""
Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor.
"""
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

#Verificando quem é o menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando quem é o maior:
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')



