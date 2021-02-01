from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - ano_nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem) '))

if dados['ctps'] != 0:
	dados['ano_contrat'] = int(input('Digite ano de contratação: '))
	dados['salario'] = float(input('Salario: '))
	dados['aposentadoria'] = dados['idade'] + ((dados['ano_contrat'] + 35) - datetime.now().year)

print('-=' * 30)
for k, v in dados.items():
	print(f'{k} tem o valor {v}')
