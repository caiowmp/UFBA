hp, vezesEspecial = map(int,input().split())
dano = 1
hp -= dano

while vezesEspecial != 0:
    especial = int(input())

    if hp <= especial:
        dano+=hp-1
        hp = 1
    else:
        hp-=especial
        dano+=especial

    vezesEspecial-=1

print(dano)