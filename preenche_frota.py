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
