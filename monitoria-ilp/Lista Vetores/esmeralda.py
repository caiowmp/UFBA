numCaixas = int(input())

entrada = input().split()

caixas = []

for i in range(numCaixas):
    caixas.append(int(entrada[i]))

sequencia = int(input())

if sequencia in caixas:
    print(sequencia)
else:
    print("-1")