instrutores = int(input())
artilheiro = 0
golsArrtilheiro = 0

while instrutores != 0:
    instrutor,gols = map(int,input().split())

    if gols > golsArrtilheiro:
        golsArrtilheiro = gols
        artilheiro = instrutor

    instrutores-=1

print("Instrutor",artilheiro)