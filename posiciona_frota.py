def posiciona_frota(infos_navios):
    tabuleiro = []

    for a in range(0, 10):
        lista_adicional = []
        
        for i in range(0, 10):
            lista_adicional.append(0)

        tabuleiro.append(lista_adicional)

    for posicoes in infos_navios.values():
        for posicao in posicoes:
            for posicao_exata in posicao:
                tabuleiro[posicao_exata[0]][posicao_exata[1]] = 1
    return tabuleiro