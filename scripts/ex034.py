#calcular aumento e informa o salario
#para salarios superior a R$ 1.250,00 - aumento de 10%
#para salarios inferior a R$ 1.250,00 - aumento de 15%
salario = float(input('Informe seu salário: '))
if salario < 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Seu novo salário será: {:.2f}'.format(novo))
