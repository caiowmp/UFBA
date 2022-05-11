qtdNumeros = int(input())

numeros =[]
impar = []
par = []

entrada = input().split()

for i in range(qtdNumeros):
    numeros.append(int(entrada[i]))

for i in range(qtdNumeros):
    if numeros[i] % 2 == 0:
        par.append(numeros[i])
    else:
        impar.append(numeros[i])

if len(par) == 0:
    par.append(" ")

if len(impar) == 0:
    impar.append(" ")

for i in range(len(par)):
    print(par[i],"",end="")

print()

for i in range(len(impar)):
    print(impar[i],"",end="")
