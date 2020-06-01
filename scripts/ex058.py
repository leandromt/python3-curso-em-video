# Melhorar jogo do desafio 28
# computar: pensar em numero de 0 a 10
# tentar adivinhar ate acertar
# mostrando no final quantos palpites foram necessarios ate acertar

import random

acertou = False
tentativas = 0

while not acertou:
    tentativas += 1
    r = random.randint(0, 10)

    print('-=' * 10)
    print('Tente adivinhar um numero..')
    print('-=' * 10)
    n = int(input('informe um numero de 0 a 10: '))

    print('{} VS {}'.format(n, r))

    if r == n:
        print('PARABENS!!! Você acertou...')
        acertou = True
    else:
        print('Você errou! Tente novamente...')

print('Quantidade de tentativas: {}'.format(tentativas))

