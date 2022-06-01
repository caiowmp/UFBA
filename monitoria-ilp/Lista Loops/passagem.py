casos = int(input())

while casos != 0:

    dias,inteira,dinheiro = input().split()
    dias = int(dias)
    inteira = float(inteira)
    dinheiro = float(dinheiro)

    while dias != 0:
        viagens = int(input())

        dinheiro-= inteira*viagens

        dias-=1

    if dinheiro >= 0:
        print("presencial")
    else:
        print("online")

    casos-=1