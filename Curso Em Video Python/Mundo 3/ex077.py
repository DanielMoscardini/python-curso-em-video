"""
Crie um programa que tenha uma tupla com varias palavras(não usar acentos). Depois disso, voce deve mostrar, para cada
palavra, quais são suas vogais.
"""
palavras = ('Aprender', 'Programar', 'Linguagem',
            'Pythonm', 'Curso', 'Gratis',
            'Estudar', 'Pratica', 'Trabalhar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
