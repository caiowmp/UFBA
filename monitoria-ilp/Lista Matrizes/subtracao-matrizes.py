linhas,colunas = map(int,input().split())

matrizA = []

for i in range(linhas):
    entrada = list(map(int,input().split()))
    matrizA.append(entrada)

matrizB = []

for i in range(linhas):
    entrada = list(map(int,input().split()))
    matrizB.append(entrada)

matrizC = []

for i in range(linhas):
    entrada = [0] * colunas
    matrizC.append(entrada)

for i in range(linhas):
    for j in range(colunas):
        matrizC[i][j] = matrizA[i][j] - matrizB[i][j]

    print(*matrizC[i])

