"""
Faça um software que leia uma frase pelo teclado e mostre:
>Quantas vezes aparece a letra "a"
>Em que posição ela aparece a primeira vez
>Em que posição ela aparece a ultima vez
"""
frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "a" apareceu: {frase.count("a")} vezes\n'
      f'A letra "a" apareceu a primeira vez na {frase.find("a")+1}º posição\n'
      f'A letra "a" apareceu a ultima vez na {frase.rfind("a")+1}º posição.')