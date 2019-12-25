#ler 5 notas
#informe qual é a maior nota e qual e a menor nota
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
n5 = float(input('Quinta nota: '))
lista = [n1, n2, n3, n4, n5]
lista.sort()
print('Sua maior nota foi {}, e sua menor nota foi {}'.format(lista[4], lista[0]))
