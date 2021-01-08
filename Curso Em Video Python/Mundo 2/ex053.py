"""
Leia uma frase qualquer e diga se ela eh um palindromo, desconsiderando os espacoes.
Ex:
-APOS A SOPA
-A SACADA DA CASA
"""
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if (inverso == junto):
    print('Temos um palindromo')
else :
    print('A frase digitada não é um palindromo')
"""
1) Pergunte uma frase pro usuário, tire os espaços e coloque tudo em minusculas
 (frase = str(input('Digite uma frase: ')).strip().lower())

2) Divida a frase com o split e junte novamente com o join, retirando os espaços.
  (
  palavras = frase.split()
  junto = ''.join(palavras)
  ) 

3) Crie o inverso, que é a frase junta, porém lida do começo até o fim, começando do final
  (
  inverso = junto[::-1]
  )
  
4) Faça a estrutura de condição, caso o inverso seja igual ao junto é um palindromo
  (
  if (inverso == junto):
    print('Temos um palindromo')
  else :
    print('A frase digitada não é um palindromo')
  )

"""



