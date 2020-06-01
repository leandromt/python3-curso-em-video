import random

fim = False


def verificaResultado(jogador, casa):

    # soma todos as cartas do jogador
    j = sum(jogador)

    # soma todos as cartas do jogador
    c = sum(casa)

    if j > 21:
        return 'Perdeu'
    if j <= 21 and j == c:
        return 'Empate'
    if j <= 21 and j > c:
        return 'Ganhou'
    else:
        return 'Perdeu'


while not fim:

    # Cartas que estao nas maos do jogadores
    mao_jogador = []
    mao_casa = []

    qtd_cartas_puxadas = 1

    while qtd_cartas_puxadas <= 3:

        print('-----------------------------------')
        print('Rodada {}'.format(qtd_cartas_puxadas))
        input('Precione enter para puxar uma carta: ')
        print('-----------------------------------')

        # monta mao do jogador
        carta_jogador = random.randint(1, 11)
        mao_jogador.append(carta_jogador)
        print('Carta do jogador: {} '.format(carta_jogador))

        # monta mao da casa
        carta_casa = random.randint(1, 11)
        mao_casa.append(carta_casa)
        print('Carta da mesa: {} '.format(carta_casa))

        print('')

        if qtd_cartas_puxadas == 3:
            resultado = verificaResultado(mao_jogador, mao_casa)
            if resultado == 'Ganhou':
                fim = True
                print('')
                print('Você ganhou!')
                print('')
            elif resultado == 'Empatou':
                print('')
                print('Você empatou!')
                print('')
            elif resultado == 'Perdeu':
                print('')
                print('Você perdeu!')
                print('')

        qtd_cartas_puxadas += 1
