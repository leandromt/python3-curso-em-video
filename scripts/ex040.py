# ler duas notas e informar e informar a media
# menor 5.0 - aprovado
# entre 5.0 e 6.9 - recuperacao
# maior igual 7.0 - aprovador

# vars
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

# output
if media < 5:
    print('Sua média foi {}. Você está reprovado!'.format(media))
elif 5 <= media < 7:
    print('Sua média foi {}. Você está de recuperação!'.format(media))
else:
    print('Sua média foi {}. Você foi aprovado. PARABÉNS!!!'.format(media))
