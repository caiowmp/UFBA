casais = int(input())

homens = list(map(int,input().split()))
homens.sort()
homens.reverse()

mulheres = list(map(int,input().split()))
mulheres.sort()

for i in range(casais):
    print(homens[i],mulheres[i])