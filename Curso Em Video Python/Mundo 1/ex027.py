"""
Faça um software que leia o nome completo de uma pessoa, mostrando em seguida, o primeiro e o ultimo nome separadamente.
ex: Ana Maria de Souza
Primeiro: Ana
Ultimo: Maria
"""
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print(f'Seu nome é: {nome}\n'
      f'Seu primeiro nome é: {nome[0]}\n'
      f'Seu ultimo nome é: {nome[len(nome)-1]}')