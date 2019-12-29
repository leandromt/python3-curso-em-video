# cores no terminal
# \033[0:33:44]m
# parametro 1 | 1 - none, 2 - bold, 4 - underline, 7 - negative
# paremetro 2 | 30 até 37
# paremetro 3 | 40 até 47

nome = 'Leandro'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pb': '\033[2;30m'
}
print('Olá, muito prazer {}{}{}. Seja bem vindo!'.format(cores['pb'], nome, cores['limpa']))
