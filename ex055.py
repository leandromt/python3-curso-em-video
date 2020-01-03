# Faça um programa que leia o peso de 5 pessoas
# No final mostre quem foi o MAIOR e o MENOR peso
pesos = []
for c in range(0, 5):
    peso = float(input('Informe o peso: '))
    pesos.append(peso)

pesos.sort()
print(pesos)
qtde = len(pesos)
print('A pessoa mais magra está com {} kg'.format(pesos[0]))
print('A pessoa mais gorda está com {} kg'.format(pesos[qtde - 1]))
