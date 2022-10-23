

#Trabalho feito usando a versão 3.10.7
from arvore import Arvore
from node import Response

def criarArquivo():
    try:        
        lerArquivo()
    except:
        arquivo = open("arquivo.bin","wb")
        arquivo.close()

def lerArquivo():
    with open("arquivo.bin") as arquivo:
        for linha in arquivo:
            chave = linha.split(' ')[0]
            if chave[0] == 'i':
                chave = chave[1:]
                nome = linha.split(' ')[1]
                idade = linha.split(' ')[2]
                inserirA(chave,nome,idade)
            else:
                chave = chave[1:]
                removerA(chave)
                continue

def escreverArquivo(chave, nome, idade):
    arquivo = open("arquivo.bin","ab+")
    conteudo = 'i' + str(chave) + ' ' + nome + ' ' + idade + '\n'
    arquivo.write(conteudo.encode('utf-8'))
    arquivo.close()

def removerArquivo(chave):
    arquivo = open("arquivo.bin","ab+")
    conteudo = 'r' + str(chave) + '\n'
    arquivo.write(conteudo.encode('utf-8'))
    arquivo.close()

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
        escreverArquivo(chave, nome, idade)
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

def inserirA(chave, nome, idade):
    chave, nome, idade
    chave = int(chave)
    dado = {"nome": nome, "idade": int(idade)}
    if arvore.inserir(chave, dado):
        return

def removerA(chave):
    arvore.remover(int(chave))

def remover():
    entrada = int(input())
    resultado = arvore.remover(entrada)
    if resultado == Response.SUCESSO:
        print("chave removida com sucesso:", entrada)
        removerArquivo(entrada)
    else:
        print("chave nao encontrada:", entrada)


def imprimir():
    arvore.imprimir()
    print()


def folhas():
    chaves = arvore.pegar_folhas()
    if len(chaves) == 0:
        print('árvore vazia')
    else:
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

criarArquivo()
while(True):
    entrada = input()
    if entrada in comandos:
        comandos[entrada]()