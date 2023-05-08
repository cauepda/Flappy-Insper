from random import *
from posicao_valida import posicao_valida
from define_posicoes import define_posicoes
from preenche_frota import preenche_frota
from posiciona_frota import posiciona_frota
from faz_jogada import faz_jogada
from embarcacoes_afundadas import afundados
seed(1)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

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

            if navios_afundados_jogador == 10:
                print('Xi! O oponente derrubou toda a sua frota =(')