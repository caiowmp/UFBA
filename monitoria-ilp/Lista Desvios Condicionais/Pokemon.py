ataque,defesa,poeira = map(int,input().split())
forca  = ataque + defesa + poeira
porcentagem = int((forca/110) * 100)

if porcentagem <= 100:
    if porcentagem <= 50:
        print("Seu pokemon nao fara progresso em batalhas")
    elif porcentagem <= 66:
        print("Seu pokemon esta acima da media")
    elif porcentagem <= 79:
        print("Seu pokemon certamente me chamou atencao")
    else:
        print("Seu pokemon e uma maravilha")
else:
    print("Hum, parece que houve um erro")
    