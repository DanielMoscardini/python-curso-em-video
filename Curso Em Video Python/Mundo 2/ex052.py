"""
Leia um numero inteiro, e diga se ele eh ou nao um numero primo
"""
num = int(input("Digite um número: "))
contador = 0

for c in range(1, num + 1):
    if num % c == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")
"""
Um numero primo tem divisão apenas 2x, ou seja:
1) Peça pro usuário escoler um numero (num = int(input("Digite um número: ")))

2) Crie um contador (contador = 0)

3) Faça uma iteração do tamanho de 1 até o numero do usuário e verifique se o mesmo é divisivél por algum numero 
que esteja entre 1 e o numero, caso seja, adicione 1 ao contador
(for c in range(1, num + 1):
    if num % c == 0:
        contador += 1)
        
4) Faça uma estrutura condicional, caso o numero de contadores(vezes que o numero foi dividido na iteração), for maior que 2,
então ele não é primo.
(if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo"))


"""
