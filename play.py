from random import *

# linha pedida n academia python
seed(1)

#------------- funções importadas ---------------------------------------
def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_ocupacao = []
    if orientacao == 'vertical':
        # coluna continua a mesma
        for i in range(0, tamanho):
            lista_ocupacao.append([linha + i, coluna])

    if orientacao == 'horizontal':
        # linha continua a mesma
        for j in range(0, tamanho):
            lista_ocupacao.append([linha, coluna + j])
    return lista_ocupacao

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    lista_nova_embarcacao = define_posicoes(linha, coluna, orientacao, tamanho)

    for a in lista_nova_embarcacao:
        if a[0] > 9 or a[1] > 9:
                    return False

    for infos in frota.values():
        qtde_embarcacoes = len(infos)

        for i in range(0, qtde_embarcacoes):
            lista_embarcacao = infos[i]

            for a in lista_nova_embarcacao:

                if a in lista_embarcacao:
                    return False
                    
    return True

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista_adicional = []

    if orientacao == 'vertical':
        for i in range(0, tamanho):
            lista_adicional.append([linha + i, coluna])

    if orientacao == 'horizontal':
        for i in range(0, tamanho):
            lista_adicional.append([linha, coluna + i])

    if nome_navio in frota and lista_adicional != []:
        frota[nome_navio] += [lista_adicional]

    if nome_navio not in frota and lista_adicional != []:
        frota[nome_navio] = [lista_adicional]

    return frota

def posiciona_frota(infos_navios):
    tabuleiro = []

    for j in range(0, 10):
        lista_adicional = []
        
        for i in range(0, 10):
            lista_adicional.append(0)

        tabuleiro.append(lista_adicional)

    for posicoes in infos_navios.values():
        for posicao in posicoes:
            for posicao_exata in posicao:
                tabuleiro[posicao_exata[0]][posicao_exata[1]] = 1
    return tabuleiro

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def afundados(frota, tabuleiro):
    navios_afundados = 0

    for infos in frota.values():
        qtde_posicoes = len(infos[0])

        for i in range(0, len(infos)):
            x = 0

            for j in range(0, len(infos[i])):

                linha = infos[i][j][0]
                coluna = infos[i][j][1]

                if tabuleiro[linha][coluna] == 'X':
                    x += 1

            if x == qtde_posicoes:
                navios_afundados += 1
    return navios_afundados

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

#------------------------------------------------------------------------------

#------------------------ criando frota jogador ------------------------
frota_jogador = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dicionario_embarcacoes = {'porta-aviões': [1, 4], 'navio-tanque': [2, 3], 'contratorpedeiro': [3, 2], 'submarino': [4, 1]}

for embarcacao, qtde in dicionario_embarcacoes.items():
    
    for i in range(0, qtde[0]):
        print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if embarcacao != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal > '))

            if orientacao == 1:
                orientacao = 'vertical'
            if orientacao == 2:
                orientacao = 'horizontal'

            if posicao_valida(frota_jogador, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota_jogador, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'
                
                frota_jogador = preenche_frota(frota_jogador, embarcacao, linha, coluna, orientacao, qtde[1])
            
            else:
                frota_jogador = preenche_frota(frota_jogador, embarcacao, linha, coluna, orientacao, qtde[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(frota_jogador, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota_jogador, linha, coluna, orientacao, qtde[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {embarcacao} que possui tamanho {qtde[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if embarcacao != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'

                frota_jogador = preenche_frota(frota_jogador, embarcacao, linha, coluna, orientacao, qtde[1])
                
            else:
                frota_jogador = preenche_frota(frota_jogador, embarcacao, linha, coluna, orientacao, qtde[1])

tabuleiro_jogador = posiciona_frota(frota_jogador)
#------------------------------------------------------------------------------------------------

#----------------------------- criando frota oponente -----------------------------
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True

lista_ataques = []

# começo do jogo
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

    if linha_ataque not in range(0, 10):
        while linha_ataque not in range(0, 10):
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

    coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

    if coluna_ataque not in range(0, 10):
        while coluna_ataque not in range(0, 10):
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual linha deseja atacar? '))

    ataque = [linha_ataque, coluna_ataque]

    if ataque in lista_ataques:
        while ataque in lista_ataques:
            print(f'A posição linha {ataque[0]} e coluna {ataque[1]} já foi informada anteriormente')

            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

            if linha_ataque not in range(0, 10):
                while linha_ataque not in range(0, 10):
                    print('Linha inválida!')
                    linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

            if coluna_ataque not in range(0, 10):
                while coluna_ataque not in range(0, 10):
                    print('Coluna inválida!')
                    coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

            ataque = [linha_ataque, coluna_ataque]

    else:
        lista_ataques.append(ataque)

        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

        navios_afundados_oponente = afundados(frota_oponente, tabuleiro_oponente)

        if navios_afundados_oponente == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
        else:
            lista_oponente = []

            linha_sorteada = randint(0, 9)
            coluna_sorteada = randint(0, 9)

            jogada = [linha_sorteada, coluna_sorteada]

            if jogada in lista_oponente:
                while jogada in lista_oponente:
                    linha_sorteada = randint(0, 9)
                    coluna_sorteada = randint(0, 9)

                    jogada = [linha_sorteada, coluna_sorteada]

            else:
                print(f'Seu oponente está atacando na linha {linha_sorteada} e coluna {coluna_sorteada}')

            tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_sorteada, coluna_sorteada)

            navios_afundados_jogador = afundados(frota_jogador, tabuleiro_jogador)

            # o jogo só para quando algum dos jogadores ganhar
            if navios_afundados_jogador == 10:
                print('Xi! O oponente derrubou toda a sua frota =(')