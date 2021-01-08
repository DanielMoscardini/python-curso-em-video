"""
Leia o nome, idade e sexo de 4 pessoas. No final mostre:
>Media de idade do grupo
>Qual eh o homem mais velho
>Quantas mulheres tem menos de 20 anos
"""
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for c in range(1, 5):
    print(f'-----{c}º PESSOA-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm': #sexo M ou m
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

mediaIdade = somaIdade / 4
print(f'A media de idade do grupo é de {mediaIdade} anos')
print(f'O homem mais velho tem {nomeVelho} e tem {maiorIdadeHomem} anos')
print(f'O total de mulheres acima de 20 anos é: {totMulher20}')