# -*- coding: utf-8 -*-

memo = {}
def fib_top_down(n):
    if n in memo :
        return memo[n]

    if n <= 2:
        f = 1 
    else:
        f = fib_top_down(n-1) + fib_top_down(n-2)
        
    memo[n] = f
    return f

casos = input()
casos = int(casos)

while casos != 0:

    numero_desejado = input()
    numero_desejado = int(numero_desejado)

    result = fib_top_down(numero_desejado)

    print("fib("+ str(numero_desejado) +") = " + str(result))

    casos -=1