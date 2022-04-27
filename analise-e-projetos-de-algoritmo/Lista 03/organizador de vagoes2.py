def insertionSort(list):
    swaps = 0
    
    for index in range(1,len(list)):
        
        value = list[index]
        pos = index
        
        while pos > 0 and list[pos - 1] > value:
            list[pos] = list[pos - 1]
            pos -= 1
            swaps +=1

        list[pos] = value

    return swaps

testes = input()
testes = int(testes)

for i in range(testes):
    tamanho = input()
    tamanho = int(tamanho)

    vagoes = [int(x) for x in input().split()]

    swaps  = insertionSort(vagoes)

    #print(vagoes,swaps)

    print("Optimal train swapping takes",swaps,"swaps.")