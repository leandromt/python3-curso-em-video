#randomizar numero de 0 a 5
#usuario tentar adivinhar o numero
#informar se ganhou ou perdeu
import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-' * 20)
num = int(input('Em que número eu pensei? '))
r = random.randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if num == r:
    print('O número sorteado foi {}'.format(r))
    print('Parabéns. Você acertou!!!')
else:
    print('O número sorteado foi {}'.format(r))
    print('Vascilou. Tente novamente...')
