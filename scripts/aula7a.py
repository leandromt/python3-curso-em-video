n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A some é {}, \n o produto é {}, a divisao é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisao inteira é {}, a potencia é {}'.format(di, e))