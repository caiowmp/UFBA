portas = int(input())
level = 1

while portas !=0:
    sigla,numero = input().split()
    numero = int(numero)

    if sigla == 't':
        level+=numero
    elif sigla == 'm':
        print("Combate iniciado")
        if numero <= level:
            level+=1
            print("VITORIA")
        else:
            print("Derrota! Fim da aventura")
            break
    elif sigla == 'b':
        if level < numero:
            level = 0
        else:
            level-=numero
    
    if level == 5:
        print("Aventura concluida")
        break


    portas-=1