matriz = []

frenetico = int(input())
res = False

for i in range(10):
    linha = list(map(int,input().split()))

    if frenetico in linha:
        res = True

    matriz.append(linha)

if res:
    print("sim")
else:
    print("nao")