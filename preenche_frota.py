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

frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)