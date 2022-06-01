valor = int(input())

entrada = input().split()

vetor = ['x'] * valor

for i in range(valor):
    vetor[i] = int(entrada[i])

if vetor[0] == 1:
    print(*vetor)
else: 
    for i in range(1,valor+1,1):
        print(vetor[-i],end=" ")