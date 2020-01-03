# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas
# No final mostre:
# 1. A média de idade do grupo
# 2. Qual é o homem mais velho
# 3. Quantas mulheres tem menos de 20 anos
idades = 0
velho_nome = ''
velho_idade = 0
mulheres = 0

for i in range(0, 4):
    nome = input('Qual o nome: ')
    idade = int(input('Qual a idade: '))
    sexo = input('Qual o sexo (M ou F): ')

    idades += idade

    if sexo == 'M' and idade > velho_idade:
        velho_nome = nome
        velho_idade = idade

    if sexo == 'F' and idade < 20:
        mulheres += 1

print('A idade média do grupo é: {}'.format(idades / 4))
print('O homem mais velho é: {}'.format(velho_nome))
print('A quantidade de mulheres menor que 20 anos é: {}'.format(mulheres))
