docesCadaParticipante,doces,participantes = map(int,input().split())

if doces >= docesCadaParticipante * participantes:
    print("YES")
else:
    print("NO")