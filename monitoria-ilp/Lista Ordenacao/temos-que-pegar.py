qtdPokemons,classificacao,ordem = input().split()
qtdPokemons = int(qtdPokemons)

pokedex = [[j for j in input().split()] for i in range(qtdPokemons)]
for i in range(qtdPokemons):
    pokedex[i][1] = int(pokedex[i][1])

for i in range(qtdPokemons-1):
    for j in range(i+1,qtdPokemons):
        if classificacao == 'L':
            if ordem == 'D':
                if pokedex[j][1] > pokedex[i][1]:
                    aux = pokedex[j][1]
                    pokedex[j][1] = pokedex[i][1]
                    pokedex[i][1] = aux
                    aux = pokedex[j][0]
                    pokedex[j][0] = pokedex[i][0]
                    pokedex[i][0] = aux
            if ordem == 'C':
                if pokedex[j][1] < pokedex[i][1]:
                    aux = pokedex[j][1]
                    pokedex[j][1] = pokedex[i][1]
                    pokedex[i][1] = aux
                    aux = pokedex[j][0]
                    pokedex[j][0] = pokedex[i][0]
                    pokedex[i][0] = aux
        if classificacao == 'N':
            if ordem == 'D':
                if pokedex[j][0] > pokedex[i][0]:
                    aux = pokedex[j][1]
                    pokedex[j][1] = pokedex[i][1]
                    pokedex[i][1] = aux
                    aux = pokedex[j][0]
                    pokedex[j][0] = pokedex[i][0]
                    pokedex[i][0] = aux
            if ordem == 'C':
                if pokedex[j][0] < pokedex[i][0]:
                    aux = pokedex[j][1]
                    pokedex[j][1] = pokedex[i][1]
                    pokedex[i][1] = aux
                    aux = pokedex[j][0]
                    pokedex[j][0] = pokedex[i][0]
                    pokedex[i][0] = aux

for i in range(qtdPokemons):
    print(*pokedex[i])