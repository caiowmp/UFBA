# -*- coding: utf-8 -*-

def MDC(a,b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a



casos = input()
casos = int(casos)

while casos != 0:
    entrada = map(int,input().split())
    a , b = entrada
    print(MDC(a,b))
    casos = casos - 1
    