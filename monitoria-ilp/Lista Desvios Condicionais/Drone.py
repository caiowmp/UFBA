coordenadaEntregaX,coordenadaEntregaY = map(int,input().split())
coordenadaDroneX,coordenadaDroneY = map(int,input().split())

if coordenadaDroneX == coordenadaEntregaX and coordenadaDroneY == coordenadaEntregaY:
    print("Soltar pacote")
else:
    print("Nao soltar pacote")
    