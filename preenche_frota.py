def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista_adicional = []

    # definindo orientações
    if orientacao == 'vertical':
        for a in range(0, tamanho):
            lista_adicional.append([linha + a, coluna])

    if orientacao == 'horizontal':
        for a in range(0, tamanho):
            lista_adicional.append([linha, coluna + a])

    if nome_navio in frota and lista_adicional != []:
        frota[nome_navio] += [lista_adicional]

    if nome_navio not in frota and lista_adicional != []:
        frota[nome_navio] = [lista_adicional]

    return frota
