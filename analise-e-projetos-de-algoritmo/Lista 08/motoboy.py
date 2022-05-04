while 1 != 0:

    pedidos = int(input())

    if pedidos == 0:
        break

    maxPizzasRob = int(input())

    pizzas = []
    tempo = []

    for i in range(pedidos):
        entrada = input().split()
        pizzas.append(int(entrada[0]))
        tempo.append(int(entrada[1]))

    print(pizzas)
    print(tempo)

    tempRob = 0

    print(tempRob,"min.")