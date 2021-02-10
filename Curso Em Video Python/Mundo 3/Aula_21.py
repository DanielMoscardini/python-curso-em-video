'''
--->Docstring
def ola(msg1, msg2):
	""" #Docstring
	->Mostra duas mensagens
	:param msg1: 1ª Mensagem
	:param msg2: 2ºMensagem
	:return:  Sem Retorno
	Função criada por DanielMoscardini
	"""
	msg1 = str(input('Digite a 1ª msg: '))
	msg2 = str(input('Digite a 2ª msg: '))
	print(msg1)
	print(msg2)


help(ola)


---->#Parâmetro Opcional
def somar(a = 0, b = 0, c=0): #Parâmetro Opcional
	print(a + b + c)

somar(3, 2, 5)

somar(8, 4)


--->#Escopo de Variavel
def teste(b):
	global a
	a = 8
	b += 4
	c = 2
	print(f'A dentro vale {a}')
	print(f'B dentro vale {b}')
	print(f'C dentro vale {c}')
	

a = 5 #A variável Global no escopo de função, sobrepoe a varável global fora da função
teste(a)
print(f'A fora vale {a}')
# print(f'No programa principal, x variável x vale {x}')


--->#Retorno de valores
def somar(a=0, b=0, c=0):
	s = a + b + c
	return s


# print(somar(3, 2, 5))
r1 = somar(2, 6, 5)
r2 = somar(3, 5)
r3 = somar(2, 23)
print(f'Meus calculos deram: r1 = {r1}, r2 = {r2} e r3 = {r3}')
'''


















