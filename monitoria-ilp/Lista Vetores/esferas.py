qtdEsferas = int(input())

entrada = input().split()

esferas = []

res = "Saia Shenlong e realize o meu desejo"

for i in range(qtdEsferas):
    esferas.append(int(entrada[i]))

boolEsferas = [False] * 7

for i in range(1,8):
    if i in esferas:
        boolEsferas[i-1] = True
        print(i,"",end="")

for i in range(7):
    if boolEsferas[i] == False:
        res = "Nao encontramos todas"

print()
print(res)