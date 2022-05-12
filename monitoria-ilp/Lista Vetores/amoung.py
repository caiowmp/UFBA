jogadores = int(input())

kills = [int(i) for i in input().split()]

aux = ['-'] * (max(kills) + 1)

for i in kills:
    aux[i] = i

for i in aux:
    if i != '-':
        print(i,end=" ")
    