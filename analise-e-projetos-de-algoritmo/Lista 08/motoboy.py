
def mochila(maxPizzasRob , pizzas , tempo , pedidos): 
  
    # Caso base
    if pedidos == 0 or maxPizzasRob == 0 : 
        return 0
  
    # Se maxPizzasRob for maior do que a cabacidade da mochila
    # então esse item não pdoe ser incluído na solução ideal
    if (pizzas[pedidos-1] > maxPizzasRob): 
        return mochila(maxPizzasRob , pizzas , tempo , pedidos-1) 
    else: 
        return max(tempo[pedidos-1] + mochila(maxPizzasRob-pizzas[pedidos-1] , pizzas , tempo , pedidos-1), 
                   mochila(maxPizzasRob , pizzas , tempo , pedidos-1)) 

while True:
    tempo = []
    pizzas = []
    pedidos = int(input())

    if pedidos == 0:
        break

    maxPizzasRob = int(input())
    
    #print(pedidos)

    for i in range(pedidos):
        entrada = list(map(int, input().split()))
        tempo.append(entrada[0])
        pizzas.append(entrada[1])
    
    print('{} min.'.format(mochila(maxPizzasRob, pizzas, tempo, pedidos)))