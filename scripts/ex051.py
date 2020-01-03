# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZAO de uma PA.
# No final, mostre os 10 primeiros termos dessa progressao
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{} '.format(i), end='-> ')
print('Acabou')
