linhas,colunas = map(int,input().split())

matriz = []

res = False

for i in range(linhas):
    entrada = list(map(int,input().split()))
    matriz.append(entrada)

tentativas = int(input())

for i in range(tentativas):
    cordL,cordC = map(int,input().split())
    matriz[cordL-1][cordC-1] = 0


for i in range(linhas):
    if 1 in matriz[i]:
        res = True

if res:
    print("ILL BE BACK")
else:
    print("HASTA LA VISTA BABY")