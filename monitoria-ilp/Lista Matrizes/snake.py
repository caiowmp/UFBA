linhas,colunas = map(int,input().split())

matriz = []
ovos = 0

for i in range(linhas):
    entrada = list(map(int,input().split()))
    matriz.append(entrada)

for i in range(linhas):
    if(i % 2 == 0):
        for j in range(colunas):
            ovos += matriz[i][j]
            if ovos < 0:
                ovos = 0
    else:
        for j in range(colunas-1,-1,-1):
            ovos += matriz[i][j]
            if ovos < 0:
                ovos = 0

print(ovos)