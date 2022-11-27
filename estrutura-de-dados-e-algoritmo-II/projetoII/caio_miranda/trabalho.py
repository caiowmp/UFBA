from dado import Dado
from arquivo import Arquivo
from arvore import Arvore

def insereTraducao(dado: Dado, contadorDeFolhas: int):
    if Arquivo.verficaSePalavraJaExiste(dado.palavra):
        print("palavra ja existente:", dado.palavra)
        return
    else:
        arvore.insereTraducao(dado, contadorDeFolhas, arvore.noRaiz)
        print('palavra inserida no dicionario: ' + dado.palavra) 
        return

def insereTraducaoInicio(dado: Dado, contadorDeFolhas: int):
    arvore.insereTraducaoInicio(dado, contadorDeFolhas, arvore.noRaiz)

def listaPalavrasCrescente():
    palavras = Arquivo.retornaPalavrasOrdemCrescente() 
    if palavras == '':
        return
    else:
        for i in palavras:
            print(i)

def listaPalavrasDecrescente():
    palavras = Arquivo.retornaPalavrasOrdemDecrescente() 
    if palavras == '':
        return
    else:
        for i in palavras:
            print(i)

def listaTraducoes(palavra: str):
    traducoes = arvore.retornaTraducoesPalavra(palavra)
    if traducoes == '':
        return
    else:
        traducoes.remove('\n')
        for i in traducoes:
            print(i)  

def listaPalavrasClasse(morfologia : str, ordem: str):
    if ordem == 'c':
        palavras = Arquivo.retornaPalavrasOrdemCrescenteMorfologia(morfologia) 
        if palavras == '':
            return
        else:
            for i in palavras:
                print(i)
    else:
        palavras = Arquivo.retornaPalavrasOrdemDecrescenteMorfologia(morfologia) 
        if palavras == '':
            return
        else:
            for i in palavras:
                print(i)

def consultaClasse(palavra: str):
    if Arquivo.verficaSePalavraJaExiste(palavra):
        morfologia = arvore.retornaMorfologiaPalavra(palavra)
        print('classe da palavra: ', palavra,':',end='',sep='')
        if morfologia == 's':
            print(' substantivo')
        elif morfologia == 'v':
            print(' verbo')
        else:
            print(' adjetivo')
    else:
        print('palavra inexistente no dicionario:', palavra)

def removePalavra(palavra: str):
    pass

def imprimeArvore():
    arvore.printaArvore(arvore.noRaiz)

    imprimePalavrasEBinarioCrescente()
    
def carregaArvore():
    arvoreAux = Arvore()

    dados = Arquivo.leArquivo()

    aux = 0
    for i in dados:
        insereTraducaoInicio(i, aux)
        aux += 1

    return arvoreAux

def imprimePalavrasEBinarioCrescente():
    palavras = Arquivo.retornaPalavrasOrdemCrescente() 
    if palavras == '':
        return
    else:
        for i in palavras:
            print(i, '', end ='')
            contBits = 0
            for j in Arquivo.retornaPalavraEmBinario(i):
                contBits += 1
                if contBits % 7 == 0:
                    print(j, '', end='')
                else:
                    print(j, end='')
            print()


arvore = Arvore()
arvore = carregaArvore()
while True:
    
    contadorDeFolhas = 0
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
        insereTraducao(Dado(palavra, morfologia, traducoes), contadorDeFolhas)
        contadorDeFolhas += 1
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