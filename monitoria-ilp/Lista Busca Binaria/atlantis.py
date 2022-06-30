largura, comprimento = map(int,input().split())

cidade = []

for i in range(largura):
    entrada = [int(x) for x in input().split()]
    for j in entrada:
        cidade.append(j)

cidade.sort()
consultas = int(input())
tempos = [int(x) for x in input().split()]

for i in tempos:
    esquerda = 0
    direita = len(cidade) - 1
    while esquerda <= direita:
        meio=(esquerda + direita) // 2
        if (i < cidade[meio]):
            direita = meio - 1
        elif(i >= cidade[meio]):
            esquerda = meio + 1
        else:
            break
    print(esquerda)