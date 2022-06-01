while True:
    nome,gols = input().split()
    gols = int(gols)

    if nome == "PELE" and gols == 1000:
        break
    elif gols > 45:
        melhor = nome
        golMelhor = gols

print(melhor,"melhor do mundo com",golMelhor,"gols.")

