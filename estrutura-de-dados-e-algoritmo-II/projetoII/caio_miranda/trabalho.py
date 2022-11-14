def insereTraducao(palavra, morfologia, traducoes):
    pass

def listaPalavrasCrescente():
    pass

def listaPalavrasDecrescente():
    pass

def listaTraducoes(palavra):
    pass

def listaPalavrasClasse(morfologia, ordem):
    pass

def consultaClasse(palavra):
    pass

def removePalavra(palavra):
    pass

def imprimeArvore():
    pass

while True:
    comando = input()

    if comando == 'e': # término da sequencia de comando
        break
    elif comando == 'i': # insere tradução
        palavra = input()
        morfologia = input()
        nTraducoes = int(input())
        traducoes = []
        for i in range(nTraducoes):
            traducoes.append(input())
        insereTraducao(palavra, morfologia, traducoes)
    elif comando == 'l': # lista palavra no idioma origem
        ordem = input()
        if ordem == 'c':    # em ordem crescente
            listaPalavrasCrescente()
        elif ordem == 'd':  # em ordem decrescente
            listaPalavrasDecrescente()
    elif comando == 't': # lista traduções
        palavra = input()
        listaTraducoes(palavra)
    elif comando == 'a': # lista palavras por classe
        morfologia = input()
        ordem = input()
        listaPalavrasClasse(morfologia, ordem)
    elif comando == 'c': # consulta classe de palavra
        palavra = input()
        consultaClasse(palavra)
    elif comando == 'r': # remove palavra
        palavra = input()
        removePalavra(palavra)
    elif comando == 'p': # imprime a árvore
        imprimeArvore()