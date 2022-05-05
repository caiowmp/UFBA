while 1 > 0:
    pedidos = int(input())

    if pedidos == 0:
        break

    capacidadeMochila = int(input())
    #cria os vetores dos pedidos considerando o pedido 0 nulo.
    pizzas = [0] * (pedidos +1)
    tempo = [0] * (pedidos + 1)

    for i in range(1,pedidos+1):
        entrada = input().split()
        tempo[i] = int(entrada[0])
        pizzas[i] = int(entrada[1])

    #criando uma tabela que tenha pedidos+1 linhas e capacidadeMochila+1 colunas.
    table = []
    linhas = [0] * (capacidadeMochila + 1)

    for i in range(pedidos+1):
        table.append(linhas)

    #a linha e a coluna 0 são sempre 0.
    
    #começando o algoritmo (preenchendo a tabela)
    #for que percorre as colunas (capacidades)
    for capacidade in range(1,capacidadeMochila):

        #for que percorre as linhas (pedidos)
        for pedido in range(1,pedidos+1):
            #se a quantidade de pizzas do pedido em questão for menor ou igual a capacidade atual
            if pizzas[pedido] <= capacidade:
                #insere na tabela, o valor máximo entre a o valor de cima e o valor da de cima na capacidade que restará mais o valor do pedido.
                if table[pedidos-1][capacidade] > table[pedidos-1][capacidade-pizzas[pedido]] + tempo[pedido]:
                    table[pedido][capacidade] = table[pedidos-1][capacidade]
                else:
                    table[pedido][capacidade] = table[pedidos-1][capacidade-pizzas[pedido]] + tempo[pedido]
            #se não, copia o valor de cima
            else:
                table[pedido][capacidade] = table[pedido-1][capacidade]

        print(table)

    print(table[pedidos][capacidadeMochila]," min.")
    table.clear()