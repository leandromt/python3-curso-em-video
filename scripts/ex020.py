#embaralhar sorteio
import random
a1 = input('Primeiro aluno: ')
a2 = input('Primeiro segundo: ')
a3 = input('Primeiro terceiro: ')
a4 = input('Primeiro quarto: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentacao será')
print(lista)