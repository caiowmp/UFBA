while True:

    vidaVamp1,vidaVamp2,ataque,dano = map(int,input().split())

    if vidaVamp1 == 0 and vidaVamp2 == 0 and ataque == 0 and dano == 0:
        break

    pDadoV1 = ataque/6
    pDadoV2 = 1 - pDadoV1

    hitsVamp1 = 0
    hitsVamp2 = 0

    while vidaVamp1 > 0:
      vidaVamp1-=dano
      hitsVamp1+=1

    while vidaVamp2 > 0:
      vidaVamp2-=dano
      hitsVamp2+=1

    #probabilidade com a moeda justa
    if pDadoV1 == 0.5:
        pTotal = 100*hitsVamp1/(hitsVamp1+hitsVamp2)
    else: #probabilidade com moeda injusta
            pTotal = 100*(1-(pDadoV2/pDadoV1)**hitsVamp1)/(1-(pDadoV2/pDadoV1)**(hitsVamp1+hitsVamp2))

    print(round(pTotal, 1))