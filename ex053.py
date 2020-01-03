# crie um programa que leia uma FRASE qualquer
# diga se ela é um PALÍNDROMO
# desconsidere os espaços

# exemplos:
# apos a sopa
# a sacada da casa
# a torre de derrota
# o lobo ama o bolo
# anotaram a data da maratona
palindromo = True
frase = input('Digite uma frase: ').strip().upper()

print('Você digitou a frase: {}'.format(frase))
palavras = frase.split()
tratado = ''.join(palavras)
inverso = tratado[::-1]
print('Frase sem espaco: ' + tratado)
print('Frase invertida: ' + inverso)
tamanho = len(tratado)
print(tamanho)
for i in range(0, tamanho):
    if tratado[i] != inverso[i]:
        print('aqui')
        palindromo = False
        break
print(palindromo)
if palindromo:
    print('É um PALÍNDROMO')
else:
    print('Não é um PALÍNDROMO')
