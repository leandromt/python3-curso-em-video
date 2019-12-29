# Calcular valor a ser pago de um produto
# A vista dinheiro / cheque 10%
# A vista cartão 5%
# 2x no cartão: preco normal
# 3x ou mais no cartao: 20% juros

produto = float(input('Informe o valor do produto: R$ '))
print('Opções de Pagamento')
print('1 - Dinheiro (10%)')
print('2 - Cheque (10%)')
print('3 - Cartão a vista (5%)')
print('4 - Cartão 2x')
print('5 - Cartão 3x ou mais (20% juros)')
op = int(input('Como você vai realizar o pagamento? '))

if op == 1:
    valor = produto - (produto * 10 / 100)
    print('O valor a ser pago será: R${} em dinheiro'.format(valor))
elif op == 2:
    valor = produto - (produto * 10 / 100)
    print('O valor a ser pago será: R${} em cheque'.format(valor))
elif op == 3:
    valor = produto - (produto * 5 / 100)
    print('O valor a ser pago será: R${} no cartão'.format(valor))
elif op == 4:
    print('O valor a ser pago será: R${} no cartão em 2x'.format(produto))
elif op == 5:
    valor = produto + (produto * 20 / 100)
    print('O valor a ser pago será: R${} no cartão em mais de 3x'.format(valor))
else:
    print('Opção não identificada!')

