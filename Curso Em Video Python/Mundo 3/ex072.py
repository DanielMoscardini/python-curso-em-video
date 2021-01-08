"""
Crie um programa que tenha uma tupla totalmente preenchida com um contagem por extenso, de zero até 20.
Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.
"""
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezenovo', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente')
print(f'Você digitou o numero {cont[num]}')
