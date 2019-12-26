#ler 3 retas
#informar se elas podem ou nao fazer um trinangulo
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
a = int(input('Reta 1: '))
b = int(input('Reta 2: '))
c = int(input('Reta 3: '))
if a < b + c and b < a + c and c < a + b:
    print('{}, {}, e {} podem formar um triângulo!'.format(a, b, c))
else:
    print('{}, {}, e {} NÃO formam um triângulo!'.format(a, b, c))
