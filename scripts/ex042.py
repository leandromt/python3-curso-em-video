# Verifica se é possivel formar um triangulo (ex035)
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = int(input('Primeiro lado: '))
r2 = int(input('Segundo lado: '))
r3 = int(input('Terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triangulo ', end='')
    # if r1 == r2 and r1 == r3 and r2 == r3:
    if r1 == r2 == r3:
        print('equilátero')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Estas retas não formam um triangulo!')


