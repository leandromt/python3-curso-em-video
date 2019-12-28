# Criar um jokenpo

from time import sleep
import emoji
from random import randint

opcoes = {
    1: ':fist:',
    2: ':raised_hand:',
    3: ':v:'
}

print('-=' * 20)
print(emoji.emojize('1 - Pedra {}'.format(opcoes[1]), use_aliases=True))
print(emoji.emojize('2 - Papel {}'.format(opcoes[2]), use_aliases=True))
print(emoji.emojize('3 - Tesoura {}'.format(opcoes[3]), use_aliases=True))
print('-=' * 20)
op = int(input('Vamos jogar? '))
pc = randint(1, 3)
# sleep(3)

print('-=' * 20)
print(emoji.emojize('{} VS {}'.format(opcoes[op], opcoes[pc]), use_aliases=True))
print('-=' * 20)

if op == pc:
    print('Empatou!')
elif (op == 1 and pc == 3) or (op == 2 and pc == 1) or (op == 3 and pc == 2):
    print('Você venceu!')
else:
    print('Você perdeu!')