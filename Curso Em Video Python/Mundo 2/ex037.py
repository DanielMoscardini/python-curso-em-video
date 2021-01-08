"""
Escreva um software que leia um numero inteiro qualquer e peça para o usuário escolher qual sera a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
"""
numero = int(input('Digite um numero inteiro: '))
print(f'Escolha a conversao de: {numero}\n'
      f'1 - Binario\n'
      f'2 - Octal\n'
      f'3 - Hexadecimal')
escolha = int(input('Qual eh sua escolha? '))
if (escolha == 1):
    print(f'{numero} em binario eh: {bin(numero)[2:]}')
elif (escolha == 2):
    print(f'{numero} em Octal eh: {oct(numero)[2:]}')
elif (escolha == 3):
    print(f'{numero} em Hexadecimal eh: {hex(numero)[2:]}')
else :
    print('Opcao Invalida, tente novamente')