def bubbleSort(array,intervalo):

    #PASSO 3:
    for i in range(len(array) - 1):
        for j in range(i+1,len(array)):
            if array[j][intervalo-1:intervalo] < array[i][intervalo-1:intervalo]:
                aux = array[i]
                array[i] = array[j]
                array[j] = aux

    print(array)

def radixSort(array):

    #PASSO 01:
    intervalo = 0
    for i in range(len(array)):
        if len(array[i]) > intervalo:
            intervalo = len(array[i])

    #PASSO 02:
    while intervalo != 0 :
        bubbleSort(array,intervalo)
        intervalo -=1


data = ["BAR","BIG","BOX","COW","DIG","DOG","EAR","FOX","MOB","NOW","ROW","RUG","SEA","TAB","TAR","TEA"]
radixSort(data)