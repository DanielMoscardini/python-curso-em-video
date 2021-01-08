"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o numero
já exista dentro da lista, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""
numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Os valores em ordem crescente são: {sorted(numeros)}')