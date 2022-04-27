# -*- coding: utf-8 -*-

casos = input()
casos = int(casos)

while casos != 0:
    numero_desejado = input()
    numero_desejado = int(numero_desejado)

    ultimo = 1
    penultimo = 1
    total = 2

    if(numero_desejado == 1) or (numero_desejado == 2):
        print(1)
    else:
        contador = 3
        while numero_desejado >= contador:
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            contador = contador + 1
            total += termo
            print(total)

        print("fib("+ str(numero_desejado) +") = " + str(total) + " calls = " + str(termo))



    casos = casos - 1