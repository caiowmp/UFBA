linhas, teleportes = list(map(int, input().split()))

matriz = []

for i in range(linhas):
    linha = list(map(int,input().split()))
    matriz.append(linha)

coordenadas = []

for i in range(teleportes):
    linha = list(map(int,input().split()))
    coordenadas.append(linha)

naves = 0
for i in coordenadas:
    x = i[0]
    y = i[1]

    for j in range(x, -1, -1):
        if matriz[j][y]: # ==1
            naves += 1
            matriz[j][y] = 0
            break

print(naves)