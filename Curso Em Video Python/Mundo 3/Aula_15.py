"""
Tuplas -> Variaveis Compostas
É uma variavel que guarda diversos valores na memorias.
Os elementos dentro da tupla são identificados por Indices, que são numéricos e começam no indice 0
Obs: AS TUPLAS SÃO IMUTÁVEIS -> Não é possivel trocar um valor dentro da tupla
Ex:
var lanche
        Hamburguer, Suco, Pizza, Pudim

            0         1     2     3

print(lanche[2]) >>> Pizza
print(lanche[0:2]) >>> Hamburguer, Suco #Exclui o ultimo numero do parametro
print(lanche[1:]) >>> Suco, Pizza, Pudim
print(lanche[-1]) >>> Pudim

len(lanche) >>> 4 #Quantidade de elementos

for c in lanche:

    print(c) >>> Hamburguer, Suco, Pizza, Pudim
"""

"""#Criando uma tupla(estrutura composta):
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[1])
print(sorted(lanche)) #Mostra em ordem e em lista
print(lanche[1:3]) #Mostra o 1 e o 2
print(lanche[2:]) #Mostra o 2 até o ultimo
print(lanche[:2]) #Mostra do inicio até o 1
print(len(lanche))
print('-'*20)

print('For com o Range: ')
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')
print('Comi para caramba!!!')

print('-'*20)

print('For sem o Range')
for c in (lanche):
    print(f'Eu vou comer {c}')
print('Comi para caramba!!!')
"""

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b #Junta as tuplas, não soma
print(c) #Mostra em ordem e em lista
print(len(c)) #Tamanho da tupla
print(c.count(5)) #Quantas vezes o numero 5 aparece em c
print(c.index(2))'''

pessoa = ('gustavo', 39, 'M', 99.88) #É possível ter dados de diferentes tipos dentro da mesma tupla
print(pessoa)