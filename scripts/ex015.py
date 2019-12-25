#aluguel de carros
dias = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos KM pecorridos? '))
custo = (60 * dias) + (km * 0.15)
print('Preço a pagar por {} dia(s) e {}km percorridos é: R${:.2f}'.format(dias, km, custo))
