# -*- coding: utf-8 -*-

def fibonacci(n,calls):

    calls += 1

    if n >= 2:
        return fibonacci(n-1,calls) + fibonacci(n-2,calls)
    else:
        return n

casos = input()
casos = int(casos)

while casos != 0:

    numero_desejado = input()
    numero_desejado = int(numero_desejado)

    calls = 0

    result = fibonacci(numero_desejado,calls)

    print("fib("+ str(numero_desejado) +") = " + str(calls) + " calls = " + str(result))

    casos -=1