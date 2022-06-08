limiteDisponivel = 1850.00
gasto = 0.00

while True:
    entrada = float(input())

    if entrada < 0.00:
        print("Numero invalido")
        break

    gasto+=entrada

    if entrada == 0.00:
        if gasto > limiteDisponivel:
            print("Passou o limite")
        else:
            limite = limiteDisponivel-gasto
            print("Valor total de %.2f e %.2f de limite disponivel" %(gasto,limite))
        
        break
        
