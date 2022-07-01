
testes = input()
testes = int(testes)

for i in range(testes):
    tamanho = input()
    tamanho = int(tamanho)

    vagoes = [int(x) for x in input().split()]

    #print(vagoes)

    swaps = 0

    for j in range(tamanho-1):
        for k in range(j+1,tamanho):
            if vagoes[j] > vagoes[k]:
                auxiliar = vagoes[j]
                vagoes[j] = vagoes[k]
                vagoes[k] = auxiliar
                swaps +=1
            
            #print(vagoes, swaps)
    
    print("Optimal train swapping takes",swaps,"swaps.")
    