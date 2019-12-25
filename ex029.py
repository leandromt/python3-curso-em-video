#ler a velocidade de um carro
#se for maior que 80km informar que foi multado
#valor da multa: R$7,00 por km acima do limite
v = int(input('Informe a velocidade (km) do carro: '))
if v > 80:
    print('Você foi multado!')
    print('Será aplicado um multa de R$ 7,00 por KM acima do limite')
    m = (v - 80) * 7
    print('Multa a pagar: R${:.2f}'.format(m))
print('Tenha um bom dia. Dirija com segurança!')
