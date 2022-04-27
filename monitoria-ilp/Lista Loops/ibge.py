entrada = int(input())
homens, mulheres = 0,0

for i in range(entrada):
    s = int(input())

    if s == 1:
        homens += 1
    elif s == 2:
        mulheres += 1

print(homens)
print(mulheres)