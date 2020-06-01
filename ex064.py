# ler varios numero inteiros
# para caso digite 999
# exibir quantos numeros foram digitados
# exibir a soma total dos numeros
# 999 - nao devera ser contabilizado (apenas apenas)

n = int(input('Digite uma número: '))
qtde = 0
soma = 0

while n != 999:
    n = int(input('Digite uma número: '))
    soma += n
    qtde += 1

print('Quantidade de números digitados: {}'.format(qtde))
print('Soma total dos números: {}'.format(soma))
