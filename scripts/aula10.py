# tempo = int(input('Quanto anos tem o seu carro? '))
# if tempo == 1:
#     print('Carro do ano!')
# elif (tempo > 1) and (tempo <= 3):
#     print('Carro ainda ta novo!')
# elif (tempo > 3) and (tempo <= 5):
#     print('Carro ainda ta novo!')
# elif (tempo > 5) and (tempo <= 10):
#     print('Carro antigo!')
# else:
#     print('Carro do tempo do bumba')
# print('fim')
n1 = float(input('Informe o valor da primeira nota: '))
n2 = float(input('Informe o valor da segunda nota: '))
media = (n1 + n2) / 2
print('Sua média foi: {:.2f}'.format(media))
#print('PARABÉNS' if media >= 7 else 'ESTUDE MAIS')
if media >= 8:
    print('PARABENS')
else:
    print('SE DEU MAL!')
