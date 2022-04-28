#caso o valor do dado seja menor ou igual ao ataque o vamp1 vence.
#quem perder, é subtraído da vida o dano e quem agnahr é somado à vida o dano.

while True:

    vidaVamp1,vidaVamp2,ataque,dano = map(int,input().split())

    if vidaVamp1 == 0 and vidaVamp2 == 0 and ataque == 0 and dano == 0:
        break

    #qual a probabilidadae do vamp1 vencer dados os valores ?

    probabilidadeDadoV1 = (ataque*100)/6
    #print(probabilidadeDadoV1)
    probabilidadeDadoV2 = 100 - probabilidadeDadoV1
    #print(probabilidadeDadoV2)

    #probabilidade com a moeda justa
    if probabilidadeDadoV1 == 50:
        probabilidadeTotal = vidaVamp1/(vidaVamp1+vidaVamp2)
    elif probabilidadeDadoV1 == 0:
        probabilidadeTotal = 0
    elif probabilidadeDadoV1 == 100:
        probabilidadeTotal == 100
    else: #probabilidade com moeda injusta
        if dano == 1:
            numerador = (1-(probabilidadeDadoV2/probabilidadeDadoV1)**vidaVamp1)
            denominador = (1-(probabilidadeDadoV2/probabilidadeDadoV1)**(vidaVamp1+vidaVamp2))
            probabilidadeTotal = numerador/denominador
        else:
            vidaVamp1 = vidaVamp1//dano
            if vidaVamp1 % dano != 0:
                vidaVamp1+=1

            vidaVamp2 = vidaVamp2//dano
            if vidaVamp2 % dano != 0:
                vidaVamp2+=1

            dano = 1

            numerador = (1-(probabilidadeDadoV2/probabilidadeDadoV1)**vidaVamp1)
            denominador = (1-(probabilidadeDadoV2/probabilidadeDadoV1)**(vidaVamp1+vidaVamp2))

            probabilidadeTotal = numerador/denominador

    print(round(probabilidadeTotal*100, 1))

    

#1 1 3 1
#1 2 1 1
#8 5 3 1
#7 5 2 4
#0 0 0 0

#50.0
#3.2
#61.5
#20.0
