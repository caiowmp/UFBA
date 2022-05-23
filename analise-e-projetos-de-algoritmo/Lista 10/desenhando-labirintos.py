def func1 (vertex, v):
    descoberta[vertex] = True
    contador = 0

    for i in range(v):
        if grafo[vertex][i] and descoberta[i] == False:
            contador += func1(i,v) + 1

    return contador

t = int(input())

while t != 0:
    n = int(input())
    v,a = map(int,input().split())

    grafo = [[0] * 49 for i in range(49)]
    descoberta = [False] * 49

    for i in range(v):
        for j in range(v):
            grafo[i][j] == 0

        descoberta[i] = False

    while a != 0:
        para,de = map(int,input().split())
        grafo[para][de] = 1
        grafo[de][para] = 1
        a-=1

    print(func1(n,v)*2)
    t-=1