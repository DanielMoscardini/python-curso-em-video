"""
Leia o ano de nascimento de 7 pessoas. No final mostre quantas pessoas ainda nao atinigiram a maioridade, e quantas
ja sao maiores.
"""
import datetime

ano = datetime.datetime.now()
menores = 0
maiores = 0
for c in range(1, 8):
    dataNasc = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = ano.year - dataNasc
    if (idade < 18):
        menores += 1
    else:
        maiores += 1
print(f'Maiores: {maiores}\n'
      f'Menores: {menores}')
