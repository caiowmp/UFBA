def fatorial(n,k):
    resultado = n
    i = 1
    while True:
        if (n-(i*k)) < 1:
            break

        resultado *= n - (i*k)
        i+=1
    
    return resultado

casos = int(input())

while(casos != 0):
    entrada = input()

    k = 0

    for i in range(len(entrada)):
        if entrada[i] == "!":
           k+=1

    #print(k)

    numero = entrada.replace("!","")
    n = int(numero)
    #print(n)

    print(fatorial(n,k))
    
    casos-=1