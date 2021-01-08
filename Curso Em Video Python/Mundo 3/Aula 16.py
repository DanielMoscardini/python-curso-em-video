"""
Listas são definidos por colchetes => []
Listas podem ser mutaveis

Para adicionar valores a uma lista(ao final da lista), utilize o metodo .append(x)

Para adicionar valores em alguma posição selecionada, utilize o metodo .insert(0, x)
# 0 é a posição e x é o valor, nesse caso, os outros valores da lista iriam "andar uma casa para frente"

Para apagar elementos de uma lista, utilize o metodo .pop(x)
# O .pop geralmente é utilizado para apagar o ultimo indice, porém é possível passar parametros para o mesmo

Para apagar um valor dentro de uma lista, utilize o metodo .remove(x)
# x é o valor que deseja apagar

# Em todos os casos de remoção, a lista é arrumada, e o indice que estava na frente do que foi removido,
# pega a posição do antigo indice, ou seja, a contagem dos indices é reposicionada
# Caso tente remover algo que não esteja na lista, acontecera erro, por isso utilize o if. exemplo:
# if 'x' in y:
#    y.remove('x')
"""
num = [2, 5, 9, 1]
num[2] = 3  # Troca o valor de 9 para 3
num.append(7)  # Adiciona o valor 7 na ultima posição da lista
num.sort(reverse=True)  # Mostra a lista em order reversa
num.insert(2, 0)  # Adiciona o 0 na posição 2 e jogo os elementos originais para frente
num.pop(2)  # Remove o 3º elemento, que se encontra no 2º indice

print(num)
print(f'Essa lista tem {len(num)} elementos')
