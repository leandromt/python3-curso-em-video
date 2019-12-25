#sortear lista de alunos
import random
a1 = input('Primeiro aluno: ')
a2 = input('Primeiro segundo: ')
a3 = input('Primeiro terceiro: ')
a4 = input('Primeiro quarto: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
#print('O aluno sorteado foi {}'.format(lista[random.randint(0,3)]))
print('O aluno sorteado foi {}'.format(escolhido))
