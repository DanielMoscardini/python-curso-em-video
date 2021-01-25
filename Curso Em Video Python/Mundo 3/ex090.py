"""
Faça um programa que leia nome e media de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteudo da estrutura na tela.
Media < 7, situação = 'RECUPERAÇÃO'
Media < 5, situação = 'REPROVADO'
"""
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno["media"] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno["media"] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
