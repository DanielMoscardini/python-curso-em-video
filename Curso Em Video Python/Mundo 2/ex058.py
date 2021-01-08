"""
Melhore o ex028, onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar
qual foi o numero até acertar. No final mostre quantos palpites foram necessários até acertar.
"""
from random import randint

maquina = randint(0,1)
print('Vou pensar em numero entre 0 e 10')
palpite = 1
usuario = int(input('Em que numero eu pensei? '))
while (usuario != maquina):
    if (usuario < maquina):
        print('Mais... Tente novamente')
    else :
        print('Menos... Tente novamente')
    usuario = int(input('Errado, tente novamente, em que numero eu pensei? '))
    palpite += 1

print(f'Você acertou!!!\n'
      f'Pensei no numero {maquina}, e você acertou com {palpite} tentativa(s) parabens, ')
