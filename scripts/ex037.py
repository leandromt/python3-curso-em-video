# conversao de bases
# 1 - binario | format(5, "b") | "{0:b}".format(5)
# 2 - octal
# 3 - hexadecimal
num = int(input('Informe um número inteiro: '))
print('''Código p/ conversão: 
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''')
op = int(input('Informe o código para converter: '))

if op == 1:
    conversao = bin(num)
    print('O número {} convertido para binário é: {}'.format(num, conversao[2:]))
elif op == 2:
    conversao = oct(num)
    print('O número {} convertido para octal é: {}'.format(num, conversao[2:]))
elif op == 3:
    conversao = hex(num)
    print('O número {} convertido para hexadecimal é: {}'.format(num, conversao[2:]))
else:
    print('Opção não encontrada!')
