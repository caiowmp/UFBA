inicio,fim = map(int,input().split())

contador = 0

for i in range(inicio,fim+1):
    multiplos = 0

    for j in range(2,i+1):
        if i % j == 0:
            multiplos +=1

    if(multiplos == 1):        
        contador +=1
        
print(contador)