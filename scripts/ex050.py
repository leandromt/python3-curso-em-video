# Crie um programa que leia 6 numeros inteiros
# E mostre a soma apenas daqueles que forem PARES
# se for IMPAR desconsidere-o

soma = 0
pares = []

for i in range(1, 6+1):
    n = int(input('Informe um número inteiro: '))
    if n % 2 == 0:
        pares.append(n)
        soma += n

print('Lista de números pares {}'.format(pares))
print('A soma dos números pares é {}'.format(soma))