# Faça um programa que calcule a SOMA entre todos os numeros IMPARES
# que sao MULTIPLOS DE 3 e que se encontram no intervalo de 1 até 500
soma = 0
for i in range(1, 500+1):
    if i % 2 != 0:
        if i % 3 == 0:
            soma += i
print(soma)