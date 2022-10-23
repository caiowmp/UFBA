from arvore import Arvore
from node import Response

GRAU_MINIMO_INDICE = 3
FATOR_CONJSEQ = 2

arvore = Arvore(GRAU_MINIMO_INDICE, FATOR_CONJSEQ)


def inserir():
    entradas = []
    for _ in range(3):
        entradas.append(input())
    chave, nome, idade = entradas
    chave = int(chave)
    dado = {"nome": nome, "idade": int(idade)}
    if arvore.inserir(chave, dado):
        print("insercao com sucesso:", chave)
        return
    print("chave ja existente:", chave)


def consultar():
    entrada = int(input())
    resultado = arvore.buscar(entrada)
    if resultado:
        nome, idade = resultado.values()
        print("chave:", entrada)
        print("nome:", nome)
        print("idade:", idade)
    else:
        print("chave nao encontrada:", entrada)


def remover():
    entrada = int(input())
    resultado = arvore.remover(entrada)
    if resultado == Response.SUCESSO:
        print("chave removida com sucesso:", entrada)
    else:
        print("chave nao encontrada:", entrada)


def imprimir():
    arvore.imprimir()


def folhas():
    chaves = arvore.pegar_folhas()
    for chave in chaves:
        print(chave)


comandos = {
    "i": inserir,
    "c": consultar,
    "p": imprimir,
    "o": folhas,
    "r": remover,
    "e": exit,
}
'''
dado = {"nome": "jonatas", "idade": 24}

chaves = [50, 30, 70,80,90,85,100,20,10,75,72,110,40]
print("\n\n Teste de inserção", chaves)

arvore = Arvore(3, 2)

for chave in chaves:
    print(chave)
    arvore.inserir(chave, dado)
    arvore.imprimir()
    print()
'''
while(True):
    entrada = input()
    if entrada in comandos:
        comandos[entrada]()

