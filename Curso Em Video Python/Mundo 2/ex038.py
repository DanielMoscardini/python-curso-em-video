"""
Escreva um software que leia dois numeros inteiros e os compare, mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais
"""
#Entrada de Dados:
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

#Processamento e saida de Dados:
if(n1 > n2) :
    print(f'Primeiro valor({n1}) eh maior que segundo valor({n2})')
elif(n2 > n1) :
    print(f'Segundo valor({n2}) eh maior que primeiro valor({n1})')
elif(n1 == n2) :
    print(f'Primeiro valor({n1}) eh igual ao segundo valor({n2})')
else :
    print('Valores Invalidos, tente novamente')