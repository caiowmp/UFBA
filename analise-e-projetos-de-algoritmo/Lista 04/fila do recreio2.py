import copy

casos = int(input())

while casos != 0:

    alunos = int(input())

    notas = list(map(int,input().split()))
    ordenado = copy.copy(notas)
    ordenado.sort(reverse=True)

    contador = 0

    for i in range(alunos):
        if(ordenado[i] == notas[i]):
            contador+=1
    
    print(contador)
    casos -=1
    