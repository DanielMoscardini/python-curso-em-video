"""
Faça um software que leia um numero de 0 a 9999 e retorne cada um dos digitos separados.
Exemplos: 1834
unidade:4
dezena:3
centena:8
milhar:1
"""
numero = int(input('Digite o valor do numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Analisando: {numero}\n'
      f'Unidade: {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}\n'
      f'Milhar: {m}\n')