"""
def soma(a, b):
	print(f'a = {a} --- b = {b}')
	print(f'A soma de {a} + {b} é de: {a + b}')
	print()


soma(4, 5)
soma(8, 9)
soma(2, 1)

---------------------------------------------------------------------------------------------------------------------

def contador(*num):  # parâmetro recebe diversos valores
	print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6)

---------------------------------------------------------------------------------------------------------------------

#Dobrando valores de uma lista
def dobra_valores(list):
	pos = 0
	while pos < len(list):
		list[pos] *= 2
		pos += 1


valores = [7, 2, 5, 0, 4]
dobra_valores(valores)
print(valores)
"""
