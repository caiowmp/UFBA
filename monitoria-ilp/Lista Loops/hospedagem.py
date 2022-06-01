amigos = int(input())
vagas = 0

while True:
    quarto = input()

    if quarto == "FIM":
        break
    elif quarto == "Casal":
        vagas+=2
    elif quarto == "Triplo":
        vagas+=3
    elif quarto == "Quadruplo":
        vagas+=4
    elif quarto == "Familia":
        vagas+=5

if vagas >= amigos:
    print("Pode reservar! Esses quartos cabem todos.")
else:
    print("Procure outra pousada.")
