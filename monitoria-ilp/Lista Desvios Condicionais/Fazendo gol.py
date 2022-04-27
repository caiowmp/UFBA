zagueiro,goleiro = input().split()
drible,chute = input().split()

if zagueiro != drible:
    print("Bloqueado")
else:
    print("Driblado")

    if goleiro != chute:
        print("...e o goleiro pega")
    else:
        print("Gol")