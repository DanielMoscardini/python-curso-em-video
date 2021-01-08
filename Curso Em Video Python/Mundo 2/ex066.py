"""
Leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o numero 999, que é a condição
de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)
"""
cont  = soma = 0
while True:
    num = int(input('Digite um numero: '))
    if (num == 999):
        break
    soma += num
    cont += 1
print(f'A soma de todos os {cont} é de {soma}')
