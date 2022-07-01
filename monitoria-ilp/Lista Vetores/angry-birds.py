partida = int(input())

vetor = [int(x) for x in input().split()]

for i in range(1,partida+1):
    print(vetor[-i],end=" ")