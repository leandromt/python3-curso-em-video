#conversor de moeadas - real para dollar
#1 dollar - 4,06 Real - em 16/12/19
v = float(input('Quanto você tem na carteira? R$ '))
print('Com R${:4.2f} você pode comprar ${:4.2f} dolares'.format(v, v / 3.27))
