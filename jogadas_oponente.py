from random import randint
from posicao_valida import posicao_valida
from define_posicoes import define_posicoes
from preenche_frota import preenche_frota
from posiciona_frota import posiciona_frota
from faz_jogada import faz_jogada
from embarcacoes_afundadas import afundados

frota = {
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

            if posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:

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
                
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])
            
            else:
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, qtde[1]) == False:

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

                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])
                
            else:
                frota = preenche_frota(frota, embarcacao, linha, coluna, orientacao, qtde[1])

print(frota)

navios_afundados = 0

tabuleiro = posiciona_frota(frota)

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

tabuleiro = faz_jogada(tabuleiro, linha_sorteada, coluna_sorteada)

navios_afundados = afundados(frota, tabuleiro)

if navios_afundados == 10:
    print('Xi! O oponente derrubou toda a sua frota =(')