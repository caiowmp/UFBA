import math
    
ponto1=list(map(float,input().split())) 
x1 = ponto1[0]
y1 = ponto1[1]   

ponto2=list(map(float,input().split())) 
x2 = ponto2[0]
y2 = ponto2[1] 

distancia = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

print('%.4f' % distancia )