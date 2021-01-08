"""
Faça um software que leia o nome de uma pessoa e retorne se ela tem "silva" no nome
"""
nome = str(input('Digite seu nome completo: ')).strip().lower()
print(f'Seu nome tem silva? {"silva" in nome} ')