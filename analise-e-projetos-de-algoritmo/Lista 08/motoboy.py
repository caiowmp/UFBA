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
    table = [[0 for _ in range(31)] for _ in range(21)]

    #a linha e a coluna 0 são sempre 0.
    
    #começando o algoritmo (preenchendo a tabela)
    #for que percorre as colunas (capacidades)
    for pedido in range(1,pedidos+1):
        #for que percorre as linhas (pedidos)
        for capacidade in range(1,capacidadeMochila+1):       
            #valor de cima
            s = table[pedido-1][capacidade]
            #se a quantidade de pizzas do pedido em questão for menor ou igual a capacidade atual
            if pizzas[pedido] <= capacidade:
                soma = table[pedido-1][capacidade-pizzas[pedido]] + tempo[pedido]
                #insere na tabela, o valor máximo entre a o valor de cima e o valor da de cima na capacidade que restará mais o valor do pedido.
                table[pedido][capacidade] = max(s,soma)
            else:
                table[pedido][capacidade] = s

    print(table[pedidos][capacidadeMochila],"min.")
    table.clear()