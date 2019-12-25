#aumento salarial
salário = float(input('Informe o valor do salário atual: R$'))
aumento = float(input('Informe a porcentagem do aumento: '))
novo = salário + (salário * aumento / 100)
print('Seu salário vai aumentar para R${:.2f}'.format(novo))
