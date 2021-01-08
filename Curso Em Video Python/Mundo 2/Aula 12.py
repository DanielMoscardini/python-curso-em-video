#Estrutura Condicional Aninhada:
nome = str(input('Qual é seu nome? ')).strip().lower()
if (nome == 'daniel'):
    print(f'Que nome Bonito!')
elif (nome == 'pedro' or nome == 'paulo' or nome == 'maria'):
    print('Seu nome é bem popular no brasil')
else:
    print('Seu nome é bem comum')
print(f'Tenha um bom dia {nome}')