#Parando uma repetição "continúa" com o break
s = n = 0
while True:
    n = int(input('Digite um numero: '))
    if (n == 999):
        break
    s += n
print(f'A soma vale {s}')
