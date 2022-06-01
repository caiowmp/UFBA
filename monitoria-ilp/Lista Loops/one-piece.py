somatorio = 0

while True:
    qtd = int(input())

    if qtd == 0:
        break

    somatorio+=qtd

if somatorio == 1000:
    print("Parabens! Voce concluiu One Piece!")
else:
    print("Caro Otaku, faltam",1000-somatorio,"eps para concluir One Piece.")
