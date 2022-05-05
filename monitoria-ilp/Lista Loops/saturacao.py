entrada_letra = "A"
entrada_numero = 1

while entrada_letra != "#" and entrada_numero != 0:
    entrada_letra,entrada_numero = input().split()
    entrada_numero = int(entrada_numero)

    if entrada_numero < 90 and entrada_numero > 0:
        print(entrada_letra,"Internar")
    elif entrada_numero >= 90:
        print(entrada_letra,"Alta")