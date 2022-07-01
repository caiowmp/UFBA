# a palavra não pode ser separada silabicamente em duas linhas

def questao(palavras,max_linhas_pg,max_char_linha,conto):

    i = 0 
    linhas = 0
    while i != len(conto):
        if (i + max_char_linha) < len(conto):
            if conto[i+max_char_linha] == " ":
                linhas += 1
                i += max_char_linha +1
            else:
                while conto[i+max_char_linha] != " ":
                    i-= 1
                linhas += 1
                i += max_char_linha +1
        else:
            linhas += 1
            break

    pags = linhas//max_linhas_pg

    if linhas % max_linhas_pg != 0:
        pags += 1

    print(pags)


while True:
    try:
        palavras, max_linhas_pg, max_char_linha = map(int,input().split())
        conto = input()
        questao(palavras,max_linhas_pg,max_char_linha,conto)
    except EOFError:
        break

#14 4 20
#Se mana Piedade tem casado com Quincas Borba apenas me daria uma esperanca colateral
#16 3 30
#No dia seguinte entrou a dizer de mim nomes feios e acabou alcunhando me Dom Casmurro
#5 2 2
#a de i de o
#5 2 2
#a e i o u
