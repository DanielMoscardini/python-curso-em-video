"""
Leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa
Realize a operação solicitada em cada caso.
"""
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
maior = 0
menor = 0
escolha = 0
while (escolha != 5):
    print(f'[1]somar valores\n'
          f'[2]multiplicar valores\n'
          f'[3]maior valor\n'
          f'[4]novos valores\n'
          f'[5]sair do programa\n')
    escolha = int(input('Qual sua escolha? '))
    if (escolha == 1):
        print(f'A soma de {n1} e {n2} é: {n1 + n2}\n')
    elif (escolha == 2):
        print(f'A multiplicação de {n1} e {n2} é: {n1 * n2}\n')
    elif (escolha == 3):
        if (n1 > n2):
            print(f'O maior valor entre {n1} e {n2} é: {n1}\n')
        else:
            print(f'O maior valor entre {n1} e {n2} é: {n2}\n')
    elif (escolha == 4):
        n1 = int(input(f'Qual é o primeiro valor? '))
        n2 = int(input(f'Qual é o segundo valor?'))
    elif (escolha == 5):
        print(f'Saindo do programa:')
    else:
        print('Escolha inválida, tente novamente: \n')

print('Fim do programa, volte sempre!!!')
