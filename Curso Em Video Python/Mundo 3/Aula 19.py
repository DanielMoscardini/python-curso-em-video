"""# É possível utilizar tuplas, listas e dicionários em conjunto.

# Criando dicionário 'dados'
dados = {'nome': 'Pedro'}  # Pedro = valor <-> nome = Identificador do elemento
print(dados['nome'])

# Como criar um novo elemento:
dados['sexo'] = 'M'
print(dados)
print(dados['sexo'])

# Como remover elementos:
del dados['sexo']
print(dados)

# Criando dicionário com vários elementos:
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme)
print(filme['ano'])"""
"""
Desse jeito, criamos a estrutura de dados 'filme', com:
3 elementos :  'titulo' - 'ano' - 'diretor' -> Python reconhece esses elementos como chaves ou keys

3 valores :  'Star Wats' - 1977 - 'George Lucas' -> Python reconhece esses valores como valores ou values

3 itens :  'titulo', 'Star Wars' - 'ano', 1997 - 'diretor', 'George Lucas' - Python reconhece esses grupos
                                                                             como itens ou items
"""

pessoas = {
    'nome': 'Gustavo', 'sexo': 'M', 'idade': 22
}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# Como esta dentro de aspas simples, referencie usando aspas duplas
# colchetes para referenciar, chaves para declarar

print(pessoas.keys())  # Mostrando as chaves
print(pessoas.values())  # Mostrando os valores
print(pessoas.items())  # Mostrando os itens. Obs: itens = PTBR / items = EN

# Mostrando as chaves com laços de repetição
for k in pessoas.keys():
    print(k)

# Mostrando as chaves com laços de repetição
for k in pessoas.values():
    print(k)

# Mostrando as chaves e os valores com laços de repetição
for k, v in pessoas.items():
    print(f'{k} = {v}')

# Criando um dicionario dentro de uma lista:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0])
print(brasil[0]['uf'])

# dicionario e lista em estrutura de repetição:
estado = {}
brasil = []
for c in range(1, 4):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
