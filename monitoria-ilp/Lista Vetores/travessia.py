numSapos,numPedras = map(int,input().split())

pedras = [0] * numPedras

for i in range(numSapos):
    pulo = int(input())

    for j in range(0,numPedras,pulo):
        pedras[j] = 1

for i in pedras:
    print(i,"",end="")