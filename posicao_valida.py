from define_posicoes import define_posicoes
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
                

