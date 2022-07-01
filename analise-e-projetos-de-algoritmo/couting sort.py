def countingSort(arr):
    size = 0
    for i in range(len(arr)):
      if arr[i] > size:
        size = arr[i]

    print("Array count inicializado e zerado:")
    count = [0] * (size + 1)
    print(count)
    print()
 
    print("Ordenando o array count com cada elemento:")
    for m in range(0, len(arr)):
        count[arr[m]] += 1
        print(count)
    print()

    print("Ordenando o array count acumulativo:")
    for m in range(1, size + 1):
        count[m] += count[m - 1]
        print(count)
    print()

    print("Array output inicializado e zerado:")
    output = [0] * len(arr)
    print(output)
    print()

    print("Colocando os elementos no array output depois de achar o index de cada elemento do array original no array count")
    for m in range(len(arr) - 1, -1,-1):
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        print(output)

    for m in range(0, len(arr)):
        arr[m] = output[m]

data = [6,0,2,0,1,3,4,6,1,3,2]
countingSort(data)
print()
print("Sorted Array: ")
print(data)
