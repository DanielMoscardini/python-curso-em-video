"""
Crie um software que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"
"""
cidade = str(input('Em qual cidade você nasceu? ')).strip().lower()
print(cidade[:5] == 'santo')