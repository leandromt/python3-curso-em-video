#Numero real para numero inteiro
#arredondando o numero para baixo

#import math
from math import floor, trunc

n = float(input('Digite um numero: '))
#inteiro = math.floor(n)
print('O numero real é {}'.format(n))
print('O numero inteiro é {}'.format(floor(n)))
print('O numero inteiro é {}'.format(int(n)))
print('O numero inteiro é {}'.format(trunc(n)))
