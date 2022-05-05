while 1 > 0:
    #n
    pedidos = int(input())

    if pedidos == 0:
        break

    #c
    capacidadeMochila = int(input())
    tempo = []
    pizzas = []

    #cria tabela
    table = []

    linha = [0] * 30

    for i in range(20):
        table.append(linha)

    for i in range(pedidos):
        entrada = list(map(int,input().split()))
        #valor
        tempo.append(entrada[0])
        #peso
        pizzas.append(entrada[1])
    
    # i = b
    for i in range(1,capacidadeMochila+1):
        #zera a primeira linha
        table[0][i] = 0

        #j = i
        for j in range(1,pedidos+1):
            s = table[j-1][i]

            #se o novo pedido nao ultrapassar a capacidade e tiver maior tempo:
            if pizzas[j-1] <= i:
                soma = table[j-1][i-pizzas[j-1]] + tempo[j-1]

                if s < soma:
                    s = soma

            table[j][i] = s

    #print(table)
    print(table[pedidos][capacidadeMochila],"min.",tempo.sum())

    #zera a tabela
    table.clear()