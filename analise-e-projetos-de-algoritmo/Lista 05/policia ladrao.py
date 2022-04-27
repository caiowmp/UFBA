# 0 pode atravessar
# 1 não pode atravessar
# PASSOU

def entrada_aberta(labirinto):
    if labirinto[0][0] == 0:
        return True

def saida_aberta(labirinto):
    if labirinto[4][4] == 0:
        return True

def direita_livre(labirinto,i,j):
    if j < 4:
        if labirinto[i][j+1] == 0:
            return True
        else:
            return False

def esquerda_livre(labirinto,i,j):
    if j > 0:
        if labirinto[i][j-1] == 0: 
            return True
        else:
            return False

def cima_livre(labirinto,i,j):
    if i > 0:
        if labirinto[i-1][j] == 0:    
            return True
        else:
            return False

def baixo_livre(labirinto,i,j):
    if i < 4:
        if labirinto[i+1][j] == 0:    
            return True
        else:
            return False

def fim(labirinto):
    if labirinto[4][4] == 5:
        print("COPS")
        return False
    else:
        print("ROBBERS")
        return True

def anda(labirinto,i,j):

    #marca as posições em que ja passei
    labirinto[i][j] = 5

    #enquanto não chegar ao fim
    while 0 < 1:
        #verifica se em baixo está livre
        if baixo_livre(labirinto,i,j):
            anda(labirinto,i+1,j)      
        #verifica se em cima está livre
        elif cima_livre(labirinto,i,j):
            anda(labirinto,i-1,j)
        #verifica se a direita está livre
        elif direita_livre(labirinto,i,j):
            anda(labirinto,i,j+1)
        #verifcia se a esquerda está livre
        elif esquerda_livre(labirinto,i,j):
            anda(labirinto,i,j-1)
        else:
            break

def print_matriz(labirinto):
    for i in range(5):
        print(list(labirinto[i]))



#MAIN:
casos = int(input())

while casos !=0:

    #lê o labirinto e ignora linhas em branco
    labirinto = []

    i = 0
    while i < 5:
        
        linha = list(map(int,input().split()))
        
        if len(linha) == 5:
            labirinto.append(linha)
            i+=1
            
    #print_matriz(labirinto)

    #verifica se a entrada e a saída estão livres e chama a função recursiva anda
    if entrada_aberta(labirinto) and saida_aberta(labirinto):
        anda(labirinto,0,0)

    fim(labirinto)

    #print_matriz(labirinto)

    casos -=1