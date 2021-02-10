"""
[:] -> cópia
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

resultado -> Joao tem 19 anos de idade / Ana tem 33 anos de idade / Joaquim tem 13 anos de idade / Maria tem 45 anos de idade
"""
maior = menor = 0
galera = []
dado = []
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Obrigatório criar a cópia
    dado.clear() #Obrigatório para não gerar copias consecutivas

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else :
        print(f'{p[0]} é, menor de idade')
        menor += 1
print(f'Temos {maior} maiores de idade e {menor} menores de idade')