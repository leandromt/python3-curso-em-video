# ler um numero qualquer e exibir seu fatorial
# Ex: 5! = 5x4x3x2x1 = 120

n = int(input('Informe um número: '))
fatorial = 1
print('{}!='.format(n), end='')
while n > 0:
    if n == 1:
        print('{}'.format(n), end='')
    else:
        print('{}*'.format(n), end='')
    n -= 1
    fatorial += fatorial * n
print('={}'.format(fatorial))