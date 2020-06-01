# ler o sexo de uma pessoa M ou F
# caso esteja errado solicitar novamente
# somente sexo valido

sexo = input('Informe o sexo. [M/F]').strip().upper()[0]

while sexo not in 'MmFf':
    sexo = input('Dados inválido! Informe o sexo. [M/F]').strip().upper()[0]
    if sexo == 'M':
        sexo_descricao = 'Masculino'
    elif sexo == 'F':
        sexo_descricao = 'Feminino'

print('Você é do sexo {}'.format(sexo_descricao))
