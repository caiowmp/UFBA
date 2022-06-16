numPlanetas = int(input())
planetas = []
prioridades = []

for i in range(numPlanetas):
    planeta,prioridade = map(int,input().split())

    planetas.append(planeta)
    prioridades.append(prioridade)

for i in range(numPlanetas-1):
    for j in range(i+1,numPlanetas):
        if prioridades[j] > prioridades[i]:
            aux = prioridades[j]
            prioridades[j] = prioridades[i]
            prioridades[i] = aux
            aux = planetas[j]
            planetas[j] = planetas[i]
            planetas[i] = aux

for i in range(numPlanetas):
    print(planetas[i],prioridades[i])