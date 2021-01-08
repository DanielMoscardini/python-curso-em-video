"""
Faça um software que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""
preco = float(input('Digite o preço original: '))
NovoPreco = preco - (preco * 5 / 100)
print(f'Preço original: {preco}     Preço desconto: {NovoPreco}')




