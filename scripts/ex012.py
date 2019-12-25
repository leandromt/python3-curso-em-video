#aplicando desconto
preço = float(input('Informe o preço do produto: R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f} está com 5% de desconto! Saindo por apenas R${:.2f}'.format(preço, novo))
