from posicao_valida import posicao_valida
from define_posicoes import define_posicoes
from preenche_frota import preenche_frota

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

            # loop para o usuário colocar a posição correta
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