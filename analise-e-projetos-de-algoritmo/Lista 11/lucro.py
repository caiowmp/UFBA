maxDias = 50

def analise(lucros,quantidadeDias,custoDia):
    maximo = 0
    maximoAtual = 0

    for dia in range(quantidadeDias):
        lucro = lucros[dia] - custoDia
        maximoAtual = max(0, maximoAtual + lucro)
        maximo = max(maximo, maximoAtual)
    
    return maximo

while True:
    try:
        dias = int(input())
        custoDia = int(input())
        lucros = [0] * maxDias

        for i in range(dias):
            lucros[i] = int(input())

        print(analise(lucros,dias,custoDia))
    except EOFError:
        break
