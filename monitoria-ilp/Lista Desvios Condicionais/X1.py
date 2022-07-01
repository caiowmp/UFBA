pontosLucas = 0
pontosPedro = 0

for i in range(3):
    lucas,pedro = map(int,input().split())
    pontosLucas += lucas
    pontosPedro += pedro
    #print(pontosLucas,pontosPedro)
if pontosLucas > pontosPedro:
    print("Lucas")
elif pontosPedro > pontosLucas:
    print("Pedro")
else:
    print("Empate")
    