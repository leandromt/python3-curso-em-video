# Verifica se é possivel formar um triangulo (ex035)
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = int(input('Primeiro lado: '))
r2 = int(input('Segundo lado: '))
r3 = int(input('Terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Este é um triangulo equilátero: ')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Este é um triangulo Escaleno: ')
    else:
        print('Este é um triangulo Isósceles: ')
else:
    print('Estas retas não formam um triangulo!')


