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