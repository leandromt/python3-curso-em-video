# leio um numero inteiro
# exibir n primeiro elementos fibonacci
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Informe um numero: '))
fibo = 0
anterior = 0
contador = 0

while contador <= n:
    fibo = fibo + anterior
    if contador == 0:
        print(f'{fibo} ', end='')
    else:
        print(f'-> {fibo} ', end='')
    anterior = contador
    contador += 1
