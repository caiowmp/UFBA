import copy

casos = int(input())

while casos != 0:

    alunos = int(input())

    notas = list(map(int,input().split()))
    ordenado = copy.copy(notas)

    for i in range(len(ordenado) - 1):
        for j in range(i+1,len(ordenado)):
            if ordenado[j] > ordenado[i]:
                aux = ordenado[j]
                ordenado[j] = ordenado[i]
                ordenado[i] = aux

    contador = 0

    for i in range(alunos):
        if(ordenado[i] == notas[i]):
            contador+=1
    
    print(contador)
    casos -=1