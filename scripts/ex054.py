# crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS
# mostre quantas já atigiram a maior idade e quantas não
# considerar 21 anos para maior idade
idades = []
qtde = 0
for i in range(0, 7):
    idade = int(input('Idade da pessoa {}: '.format(i)))
    idades.append(idade)

print(idades)
for p in idades:
    if p >= 21:
        qtde += 1

if qtde > 0:
    print('{} são maiores de idade'.format(qtde))
else:
    print('Não existe pessoa maior de idade!')
