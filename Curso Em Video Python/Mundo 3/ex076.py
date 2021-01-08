"""
Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""
listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Cadeno', 15.90,
            'Estojo', 25,
            'Compasso', 9.99)
print('-' * 40)
print(f'{"Listagem de preço":^40}')
print('-' * 40)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>7.2f}')
print('-' * 40)