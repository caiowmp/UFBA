selecionados,total = map(int,input().split())

candidatos = [[int(j) for j in input().split()] for i in range(total)]

candidatos.sort()
candidatos.reverse()

for i in range(total-1):
    for j in range(i+1,total):
        if candidatos[i][0] == candidatos[j][0] and candidatos[i][1] > candidatos[j][1]:
            aux = candidatos[i]
            candidatos[i] = candidatos[j]
            candidatos[j] = aux

passaram = []

for i in range(selecionados):
    passaram.append(candidatos[i])

consulta = int(input())

for i in range(consulta):
    candidato = list(map(int,input().split()))

    if candidato in passaram:
        print("Sim")
    else:
        print("Nao")
