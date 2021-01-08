"""
Faça um software que faça o computador retornar um numero inteiro entre 0 e 5, e peça para o usuário tentar descobrir qual foi o numero
escolhido pelo computador. O programa devera escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
maquina = randint(0,5)
print('Vou pensar em numero entre 0 e 5')
usuario = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if(usuario == maquina) :
    print(f'A Máquina escolheu {maquina} e você escolheu {usuario}, você ACERTOU')
else :
    print(f'A Máquina escolheu {maquina} e você escolheu {usuario}, você ERROU')


