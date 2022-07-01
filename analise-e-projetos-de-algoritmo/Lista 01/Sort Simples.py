# -*- coding: utf-8 -*-

x = input().split()
a, b, c = x
a = int(a)
b = int(b)
c = int(c)

#sort
if a > b and a > c:
    maior = a
    if b > c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b

if b > a and b > c:
    maior = b
    if a > c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a

if c > a and c > b:
    maior = c
    if a > b:
        meio = a
        menor = b
    else:
        menor = a
        meio = b

#ordenado
print(menor)
print(meio)
print(maior)

#quebra de linha
print()

#entrada
print(a)
print(b)
print(c)

