# refaça o desafio 09
# mostrar tabuada de um numero escolhido pelo usuário utilizando for

# input
n = int(input('Informe um número inteiro: '))

# interaction
for i in range(1, 10+1):
    print('{:2} x {:2} = {:2}'.format(i, n, i*n))
