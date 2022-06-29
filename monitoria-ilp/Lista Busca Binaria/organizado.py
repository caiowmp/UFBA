qtdPlanetas = int(input())

planetas = [int(x) for x in input().split()]

planeta = list(map(int,input().split()))

for i in range(len(planeta)-1):
    esquerda = 0
    direita = qtdPlanetas - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if planeta[i] == planetas[meio]:
            break
        elif planeta[i] < planetas[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1
    if planetas[meio] == planeta[i]:
        print(meio)
    else:
        print("Nao foi visitado ainda.") 
