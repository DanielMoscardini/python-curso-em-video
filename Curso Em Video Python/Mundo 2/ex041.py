"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade:
-até 9 anos: MIRIM
-até 14 anos: INFANTIL
-até 19 anos: JUNIOR
-até 25 anos: SENIOR
-acima: MASTER
"""
#Entrada de dados:
import datetime
anoNasc = int(input('Em que ano voce nasceu? '))
anoAtual = datetime.datetime.now()
idade = anoAtual.year - anoNasc

#Processamento e saida de dados:
if ( 9 >= idade >= 1):
    print(f'O atleta tem: {idade}\nClassificacao: MIRM')
elif (14 >= idade >= 10):
    print(f'O atleta tem: {idade}\nClassificacao: INFANTIL')
elif (19 >= idade >= 11):
    print(f'O atleta tem: {idade}\nClassificacao: JUNIOR')
elif (25 >= idade >= 20):
    print(f'O atleta tem: {idade}\nClassificacao: SENIOR')
else :
    print(f'O atleta tem: {idade}\nClassificacao: MASTER')
