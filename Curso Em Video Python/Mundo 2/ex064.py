"""
Leia varios numeros inteiros. O programa só deve parar quando o usuário digitar 999, que é a condição de parada.
No final, mostre quantos numeros foram digitados e qua foi a soma entre eles, desconsiderando o flag
"""
num = cont = soma = 0
num = int(input('Digite um numero: [999 para parar] '))
while (num != 999):
    soma += num
    cont += 1
    num = int(input('Digite um numero: [999 para parar] '))
print(f'Você digitou {cont} numeros e a soma entre eles é de {soma}')