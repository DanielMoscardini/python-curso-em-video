"""
Escreva um software para aprovar o emprestimo bancario para a compra de uma casa, o programa vai perguntar o valor
da casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo sera negado.
"""
#Entrada de Dados:
valorCasa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o salário do comprador: '))
anosPagar = int(input('Em quantos anos quer financiar: '))

#Processamento:
prestacaoMensal = valorCasa / (anosPagar * 12)
if (prestacaoMensal > (salario - (salario * 70 / 100))) :
    print(f'Mensalidade: {prestacaoMensal:.2f}, é maior do que 30% de {salario} -> FINANCIAMENTO NEGADO')
else :
    print(f'Mensalidade: {prestacaoMensal:.2f}, é menor do que 30% de {salario} -> FINANCIAMENTO PERMITIDO')