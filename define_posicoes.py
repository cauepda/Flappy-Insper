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