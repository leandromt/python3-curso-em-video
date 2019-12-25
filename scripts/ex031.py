#perguntar a distancia da viagem em km
#calcular o preco da viagem
#R$ 0,50 por km para viagens ate 200km
#R$ 0,45 por km para viagens mais longas
km = int(input('Qual a distancia(km) da sua viagem? '))
'''if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45'''
preco = km * 0.50 if km <= 200 else km * 0.45

print('O preço da sua viagem será: R${:.2f}'.format(preco))