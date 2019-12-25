# ler um ano e informar se ele e bissexto
# INFORMACOES DO ANO BISSEXTO
#Anos divisíveis pelo número 4 são considerados bissextos.
#Anos divisíveis por 100 não são bissextos.
#Anos divisíveis por 400 são bissextos.
from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para buscar o ano atual '))
if ano == 0:
    #search current year
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))
