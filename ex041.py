# informar a categoria de um atleta
# até 9 anos - Mirim
# Até 14 anos - Infantil
# Até 19 anos - Junior
# Até 20 anos - Sênior
# Acima: Master

# var
idade = int(input('Informe a sua idade: '))

# output
if idade <= 9:
    print('Sua categoria é: Mirim')
elif 9 < idade <= 14:
    print('Sua categoria é: Infantil')
elif 14 < idade <= 19:
    print('Sua categoria é: Junior')
elif 19 < idade <= 20:
    print('Sua categoria é: Sênior')
else:
    print('Sua categoria é: Master')
