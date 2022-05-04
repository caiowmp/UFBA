# -*- coding: utf-8 -*-

casos = input()
casos = int(casos)

memo = {}

def fib_botom_up(n):
    memo[0] = memo[1] = 1

    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

while casos != 0:
    numero_desejado = int(input())

    res = fib_botom_up(numero_desejado)

    print("fib(",numero_desejado,") = ",res,sep="")


    casos = casos - 1