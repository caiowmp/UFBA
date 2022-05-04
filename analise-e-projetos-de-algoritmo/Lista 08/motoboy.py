while 1 != 0:

    pedidos = int(input())

    if pedidos == 0:
        break

    maxPizzasRob = int(input())
    pizzasRob = 0
    tempRob = 0

    pizzas = []
    tempo = []

    for i in range(pedidos):
        entrada = input().split()
        tempo.append(int(entrada[0]))
        pizzas.append(int(entrada[1]))

    for i in range(len(pizzas)-1):
        for j in range(i+1,len(pizzas)):
            if tempo[j] > tempo[i]:
                aux = pizzas[j]
                pizzas[j] = pizzas[i]
                pizzas[i] = aux
                aux = tempo[j]
                tempo[j] = tempo[i]
                tempo[i] = aux

    i = -1

    while i < len(pizzas)-1:
        if pizzasRob + pizzas[i+1] <= maxPizzasRob:
            pizzasRob += pizzas[i+1]
            tempRob += tempo[i+1]
            print("pizzasRob:",pizzasRob)
            print("tempRob:",tempRob)

        i+=1

    print(tempRob,"min.")