"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo!)

Saída:
-----------
Olá, Mundo!
-----------
"""

#Colocando '+4' e '2 espaços antes e depois' para ficar centralizado.
def escreva(msg):
	tam = len(msg) + 4
	print('-' * tam)
	print(f'  {msg}')
	print('-' * tam)


escreva('Hello World')
