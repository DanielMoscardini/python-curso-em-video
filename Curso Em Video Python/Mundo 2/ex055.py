"""
Leia o peso de cinco pessoas, e no final mostre o maior e o menor peso lidos
"""
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Qual é o peso da {c}º pessoa? '))
    if (c == 1):
        maior = peso
        menor = peso
    else:
        if (peso > maior):
            maior = peso
        if (peso < menor):
            menor = peso
print(f'O maior peso lido foi de {maior}Kg\n'
      f'O menor peso lido foi de {menor}Kg')

"""
1) Criar variaveis para receber o maior e o menor peso:
    maior = 0
    menor = 0

2) Fazer a iteração percorrendo de 1 a 5, e perguntar quais são os pesoas das pessoas:
    for c in range(1, 6):
        peso = float(input(f'Qual é o peso da {c}º pessoa? '))  

3) Fazer estrutura condicional, dizendo que o primeiro valor é o maior e o menor valor ao mesmo tempo, e que quando não
for, é porque algum outro valor foi adicionado, nesse caso se peso for maior do que a variavel maior, maior recebera peso
e caso o peso for menor do que a variavel menor, menor recebera peso. Dentro da iteração isso percorrerá todo os pesos,
colocando o maior na variavel maior, e o menor na variavel menor
        if (c == 1):
            maior = peso
            menor = peso
        else:
            if (peso > maior):
                maior = peso
            if (peso < menor):
                menor = peso
"""