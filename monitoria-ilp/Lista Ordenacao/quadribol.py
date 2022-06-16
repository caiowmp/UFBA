candidatos = int(input())

tempos = list(map(int,input().split()))

tempos.sort()

for i in range(8):
    print(tempos[i],end=" ")