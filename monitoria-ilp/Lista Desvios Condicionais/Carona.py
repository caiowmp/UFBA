doces = int(input())
chapeuzinho,vo,lobo = 0,0,0

#for i in range(doces,0,-1):
#if chapeuzinho == vo and vo == lobo:
    #chapeuzinho += 1
#elif chapeuzinho > vo and vo == lobo:
    #vo += 1
#else:
    #lobo +=1

chapeuzinho += doces//3
vo += doces//3
lobo += doces//3

if doces % 3 == 1:
    chapeuzinho += 1
elif doces % 3 == 2:
    chapeuzinho +=1
    vo += 1
    


print("Chapeuzinho Vermelho",chapeuzinho)
print("Vovozinha",vo)
print("Lobo Mau",lobo)
