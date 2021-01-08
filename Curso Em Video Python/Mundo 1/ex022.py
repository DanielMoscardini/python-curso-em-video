"""
Crie um software que leia o nome completo da pessoa e retorne:
>Nome com todas as letras em maiusculo
>Nome com todas as letras em minusculo
>Quantas letras ao todo, sem considerar espaços
>Quantas letras tem o primeiro nome
"""
NomeCompleto = str(input('Digite seu nome completo: ')).strip()
print(f'Letras maiúsculas: {NomeCompleto.upper()}\n'
      f'Letras minúsculas: {NomeCompleto.lower()}\n'
      f'Nome completo: {len(NomeCompleto) - NomeCompleto.count(" ")}\n'
      f'Letras no primeiro nome: {NomeCompleto.find(" ")}')

