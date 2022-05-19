inicio,fim = map(int,input().split())

contador = 0

for i in range(inicio,fim+1):
    multiplos = 0
    #print("Numero sendo anlisado:",i)

    for j in range(1,i+1):
        #print("Verificando se",i,"é divisível por",j)
        if i % j == 0:
            multiplos += 1
            #print("Multiplo encontrado:",multiplos)
  
    if multiplos == 2:
        contador += 1
        #print("Número primo encontrado:",contador)
    
print(contador)