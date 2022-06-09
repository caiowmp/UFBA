matriz = []

for i in range(10):
    linha = list(input().split())
    matriz.append(linha)

for i in range(10):
    for j in range(10):
        if matriz[i][j] == 't':
            if i == 0:
                if matriz[i+1][j] == '*':
                    matriz[i][j] = 'p'
            elif i == 9:
                if matriz[i-1][j] == '*':
                    matriz[i][j] = 'p'       
            else:
                if matriz[i+1][j] == '*' or matriz[i-1][j] == '*':
                    matriz[i][j] = 'p'         
            if j == 0:
                if matriz[i][j+1] == '*':
                    matriz[i][j] = 'p'
            elif j == 9:
                if matriz[i][j-1] == '*':
                    matriz[i][j] = 'p'       
            else:
                if matriz[i][j-1] == '*' or matriz[i][j+1] == '*':
                    matriz[i][j] = 'p'
for i in range(10):
    print(*matriz[i])
