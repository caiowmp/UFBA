dimensao = int(input())

u = []

entradas = input().split()

for i in range(dimensao):
    u.append(int(entradas[i]))

v = []

entradas = input().split()

for i in range(dimensao):
    v.append(int(entradas[i]))

d = []

entradas = input().split()

for i in range(dimensao):
    d.append(int(entradas[i]))


res = "OK"

for i in range(dimensao):
    if u[i] + v[i] != d[i]:
        res = "NOPE :("

print(res)