# aprovar emprestimo bancário
# calcular emprestimo mensal
# nao pode exceder 30% do salario
# informar se foi aprovado ou não

# entradas
valor = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))

# logica
meses = anos * 12
parcela = valor / meses
limiteParcela = (salário * 30 / 100)

# saida
if parcela <= limiteParcela:
    print('Financiamento APROVADO! Sua parcela ficou {:.2f} em {} meses'.format(parcela, meses))
else:
    print('Financiamento REPROVADO! Sua parcela ficou {:.2f} em {} meses'.format(parcela, meses))
