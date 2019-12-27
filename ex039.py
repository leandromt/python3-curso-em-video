# ler ano de uma pessoa e informar a situação de alistamento militar
# Se ele ainda vai se alistar ao serviço militar (quanto tempo falta?)
# Se é hora de se alistar
# Se já passou o tempo de se alistar (quanto tempo passou)

from datetime import datetime

# vars
ano = int(input('Informe o seu ano de nascimento: '))
atual = datetime.today().year
idade = atual - ano

# logic
if idade < 18:
    diferenca = 18 - idade
    print('Você ainda vai se alistar no serviço militar! Faltam {} ano(s)'.format(diferenca))
elif idade > 18:
    diferenca = idade - 18
    print('Já passou {} ano(s) do seu período de alistamento militar!'.format(diferenca))
else:
    print('Você está com 18 anos de idade! Está no seu período de alistamento militar!')
