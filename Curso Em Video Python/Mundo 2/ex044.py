"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
-a vista dinheiro/cheque: 10% de desconto
-a vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
"""
precoAtual = float(input('Qual o valor da compra? '))
print(f'FORMA DE PAGAMENTO: \n'
      f'[1] a vista dinheiro/cheque (10% desconto)\n'
      f'[2] a vista cartao (5% desconto)\n'
      f'[3] 2x no cartao (preco normal)\n'
      f'[4] 3x ou mais no cartao (20% de juros)')
formaPagamento = int(input('Qual eh a forma de pagamento? '))
if (formaPagamento == 1) :
    print(f'Compra a vista no dinheiro/cheque de R${precoAtual}\n'
          f'PRECO COM DESCONTO DE 10%: R${precoAtual - (precoAtual * 10 / 100)}')
elif (formaPagamento == 2) :
    print(f'Compra a vista no cartao de R${precoAtual}\n'
          f'PRECO COM DESCONTO DE 5%: R${precoAtual - (precoAtual * 5 / 100)}')
elif (formaPagamento == 3) :
    print(f'Compra parcelada 2x no cartao de R${precoAtual / 2}\n')
elif (formaPagamento == 4) :
    parcelasForma4 = int(input('Em quantas parcelas? '))
    print(f'Compra parcelada em {parcelasForma4}x de R${((precoAtual + (precoAtual * 20 / 100)) / parcelasForma4)}\n'
          f'PRECO COM JUROS: R${precoAtual + (precoAtual * 20 / 100)}')
else :
    print('OPCAO INVALIDA, tente novamente\n'
          f'Sua compra de {precoAtual} vai custar RS0,00')
