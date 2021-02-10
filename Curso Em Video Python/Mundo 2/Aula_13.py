# Lacos de repeticao/iteracao
"""
#Contando de 0 a 9, pois Python ignora o ultimo numero do parametro:
for c in range (0, 10):
    print(c)
"""


"""#Contado de 10 a 1, -1 inverte a contagem da iteracao:
for c in range (10, 0, -1):
    print(c)
"""


"""
#De 0 a 10 pulando de 2 em 2:
for c in range (0, 11, 2):
    print(c)
"""

"""
#Declarando um contador e usando o mesmo de parametro:
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
"""

"""
#Definindo todas os parametros:
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
"""

"""
#Multiplos inputs em uma unica variavel
soma = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    soma += n
print(f'O somatorio de todos os valores foi: {soma}')
"""
