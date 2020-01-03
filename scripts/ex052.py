# Faça um programa que leia um número inteiro
# e diga se ele é ou não um NÚMERO PRIMO
n = int(input('Informe um número: '))
qtde = 0
for i in range(1, n + 1):
    if n % i == 0:
        qtde += 1
if qtde == 2:
    print('{} é um número primo!'.format(n))
else:
    print('{} não é um número primo!'.format(n))
