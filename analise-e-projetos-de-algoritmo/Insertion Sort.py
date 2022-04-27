input = [1,8,2,6,7,9,0,4,5,3]
# inserir a sua resposta aqui...

def insertionSort(list):
    swaps = 0
    
    for index in range(1,len(list)):
        
        value = list[index]
        pos = index
        
        while pos > 0 and list[pos - 1] > value:
            list[pos] = list[pos - 1]
            pos -= 1

        list[pos] = value

# Verificar o seu funcionamento
input = [1,8,2,6,7,9,0,4,5,3]
insertionSort(input)
print(input)