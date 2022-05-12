jogadores = int(input())

kills = [int(i) for i in input().split()]

for i in range(jogadores):
    print(min(kills),"",end="")
    kills.remove(min(kills))