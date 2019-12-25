nome = input('Informe seu nome: ')
#todas as letras maiusculas
print(nome.upper())
#todas as letras minusculos
print(nome.lower())
#qtde letras sem espacos
print('quantidade sem espaco é {}'.format(len(nome) - nome.count(' ')))
semespaco = nome.replace(' ', '')
print(len(semespaco))
#qtde letras primeiro nome
dividido = nome.split()
print(len(dividido[0]))
