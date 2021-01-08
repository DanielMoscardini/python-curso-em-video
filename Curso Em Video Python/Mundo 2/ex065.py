"""
Leia varios numeros inteiros. No final da execução, mostre a media entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer continuar ou não digitando valores.
"""
media = quant = soma = maior = menor = 0
resp = 'S'
while (resp in 'sS'):
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if (quant == 1):
        maior = menor = num
    else:
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / quant
print(f'Você digitou {quant} e a media foi {media}')
print(f'O maior numero foi {maior} e o menor numero foi {menor}')
