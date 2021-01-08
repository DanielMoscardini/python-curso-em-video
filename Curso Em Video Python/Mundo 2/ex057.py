"""
Leia o sexo de uma pessoa, mas só aceite M ou F. Caso esteja errado, peça digitação novamente, até ter um valor estar correto.
"""
sexo = str(input('Qual seu sexo? [M/F]')).strip().upper()[0]
while (sexo not in 'MF'):
    sexo = str(
        input('Mensagem Inválida, qual seu sexo? [M/F]')).strip().upper()[0]

print(f'Sexo {sexo} cadastrado com sucesso!!!')
