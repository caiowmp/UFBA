from no import No
from dado import Dado
from arquivo import Arquivo

class Arvore:
    def __init__(self):
        self.noRaiz = No(0)

    def insereTraducao(self, dado: Dado, posArquivo: int, noBase: No):
        caminho0 = noBase.ponteiro0
        caminho1 = noBase.ponteiro1
        palavraEmBinario = dado.retornaPalavraEmBinario()
        if len(palavraEmBinario) >= noBase.bitComparavel:
            if palavraEmBinario[noBase.bitComparavel] == 1: # seguindo o caminho1
                if caminho1 == -1: # caso caminho1 esteja vazio
                    noBase.ponteiro1 = posArquivo  
                elif isinstance(caminho1, int): # Caso o caminho aponte para a posição de uma palavra
                    palavraEmBinarioFolha = Arquivo.lePosicaoArquivo(caminho1).retornaPalavraEmBinario() # Pega a palavra sendo apontada
                    posAntiga = caminho1 # Armazena a posição da palavra que estava no ponteiro
                    bitComparavelNovoNo = self.comparaPalavras(palavraEmBinario, palavraEmBinarioFolha, noBase.bitComparavel)
                    if noBase.bitComparavel > bitComparavelNovoNo:
                        #if noBase == self.noRaiz:
                            novoNo = No(bitComparavelNovoNo)
                            if palavraEmBinarioFolha[bitComparavelNovoNo] == 1:
                                novoNo.caminho1 = noBase
                                novoNo.caminho0 = posArquivo
                            else:
                                novoNo.caminho0 = noBase
                                novoNo.caminho1 = posArquivo
                            noBase = novoNo
                    caminho1 = No(bitComparavelNovoNo) # Cria um novo nó que irá apontar e que vai conter as duas palavras
                    noBase.ponteiro1 = caminho1
                    if palavraEmBinario[bitComparavelNovoNo] == 1:
                        caminho1.ponteiro1 = posArquivo 
                        caminho1.ponteiro0 = posAntiga
                    else:
                        caminho1.ponteiro0 = posArquivo 
                        caminho1.ponteiro1 = posAntiga
                else: # Caso o caminho1 aponte pra outro nó
                    self.insereTraducao(dado, posArquivo, caminho1)
        else: # seguindo o caminho 0
            if caminho0 == -1: # caso o caminho0 esteja vazio
                noBase.ponteiro0 = posArquivo
            elif isinstance(caminho0, int): # Caso o caminho aponte para a posição de uma palavra
                palavraEmBinarioFolha = Arquivo.lePosicaoArquivo(caminho0).retornaPalavraEmBinario() # Pega a palavra sendo apontada
                posAntiga = caminho0 # Armazena a posição da palavra que estava no ponteiro
                bitComparavelNovoNo = self.comparaPalavras(palavraEmBinario, palavraEmBinarioFolha, noBase.bitComparavel)
                if noBase.bitComparavel > bitComparavelNovoNo:
                    novoNo = No(bitComparavelNovoNo)
                    if palavraEmBinarioFolha[bitComparavelNovoNo] == 1:
                        novoNo.caminho1 = noBase
                        novoNo.caminho0 = posArquivo
                    else:
                        novoNo.caminho0 = noBase
                        novoNo.caminho1 = posArquivo
                caminho0 = No(bitComparavelNovoNo) # Cria um novo nó que irá apontar e que vai conter as duas palavras
                noBase.ponteiro0 = caminho0
                if palavraEmBinario[bitComparavelNovoNo] == 1:
                    caminho0.ponteiro1 = posArquivo 
                    caminho0.ponteiro0 = posAntiga
                else:
                    caminho0.ponteiro0 = posArquivo 
                    caminho0.ponteiro1 = posAntiga
            else: # Caso o caminho0 aponte pra outro nó
                self.insereTraducao(dado, posArquivo, caminho0)                
        Arquivo.escreveArquivo(dado)

    # função para carregar a arvore ao iniciar o programa
    def insereTraducaoInicio(self, dado: Dado, posArquivo: int, noBase: No):
        caminho0 = noBase.ponteiro0
        caminho1 = noBase.ponteiro1
        palavraEmBinario = dado.retornaPalavraEmBinario()
        if len(palavraEmBinario) >= noBase.bitComparavel:
            if palavraEmBinario[noBase.bitComparavel] == 1: 
                if caminho1 == -1: 
                    noBase.ponteiro1 = posArquivo  
                elif isinstance(caminho1, int): 
                    palavraEmBinarioFolha = Arquivo.lePosicaoArquivo(caminho1).retornaPalavraEmBinario() 
                    posAntiga = caminho1 
                    bitComparavelNovoNo = self.comparaPalavras(palavraEmBinario, palavraEmBinarioFolha, noBase.bitComparavel)
                    if noBase.bitComparavel > bitComparavelNovoNo:
                        novoNo = No(bitComparavelNovoNo)
                        if palavraEmBinarioFolha[bitComparavelNovoNo] == 1:
                            novoNo.caminho1 = noBase
                            novoNo.caminho0 = posArquivo
                        else:
                            novoNo.caminho0 = noBase
                            novoNo.caminho1 = posArquivo
                    caminho1 = No(bitComparavelNovoNo)
                    noBase.ponteiro1 = caminho1
                    if palavraEmBinario[bitComparavelNovoNo] == 1:
                        caminho1.ponteiro1 = posArquivo 
                        caminho1.ponteiro0 = posAntiga
                    else:
                        caminho1.ponteiro0 = posArquivo 
                        caminho1.ponteiro1 = posAntiga
                else: 
                    self.insereTraducaoInicio(dado, posArquivo, caminho1)
        else: 
            if caminho0 == -1: 
                noBase.ponteiro0 = posArquivo
            elif isinstance(caminho0, int):
                palavraEmBinarioFolha = Arquivo.lePosicaoArquivo(caminho0).retornaPalavraEmBinario() 
                posAntiga = caminho0 
                bitComparavelNovoNo = self.comparaPalavras(palavraEmBinario, palavraEmBinarioFolha, noBase.bitComparavel)
                if noBase.bitComparavel > bitComparavelNovoNo:
                    novoNo = No(bitComparavelNovoNo)
                    if palavraEmBinarioFolha[bitComparavelNovoNo] == 1:
                        novoNo.caminho1 = noBase
                        novoNo.caminho0 = posArquivo
                    else:
                        novoNo.caminho0 = noBase
                        novoNo.caminho1 = posArquivo
                caminho0 = No(bitComparavelNovoNo)
                noBase.ponteiro0 = caminho0
                if palavraEmBinario[bitComparavelNovoNo] == 1:
                    caminho0.ponteiro1 = posArquivo 
                    caminho0.ponteiro0 = posAntiga
                else:
                    caminho0.ponteiro0 = posArquivo 
                    caminho0.ponteiro1 = posAntiga
            else: 
                self.insereTraducaoInicio(dado, posArquivo, caminho0)

    def comparaPalavras(self, palavraEmBinario, palavraEmBinarioFolha, bitComparavel):
        if len(palavraEmBinario) < len(palavraEmBinarioFolha): 
            tam = len(palavraEmBinario)
            for i in range(tam):
                if palavraEmBinario[i] != palavraEmBinarioFolha[i]:
                    return i
            return tam + 1 
        elif len(palavraEmBinario) > len(palavraEmBinarioFolha):
            tam = len(palavraEmBinarioFolha)
            for i in range(tam):
                if palavraEmBinario[i] != palavraEmBinarioFolha[i]:
                    return i
            return tam + 1
        else:
            tam = len(palavraEmBinarioFolha)
            for i in range(tam):
                if palavraEmBinario[i] != palavraEmBinarioFolha[i]:
                    return i
            return tam + 1

    def retornaPosicaoPalavra(self, palavra: str, noBase: No):
        palavraEmBinario = Arquivo.retornaPalavraEmBinario(palavra)
        caminho0 = noBase.ponteiro0
        caminho1 = noBase.ponteiro1
        if palavraEmBinario[noBase.bitComparavel] == 1: # seguindo o caminho1
            if caminho1 == -1: # caso caminho1 esteja vazio
                return -1
            elif isinstance(caminho1, int): # Caso o caminho aponte para a posição de uma palavra
                return caminho1
            else: # Caso o caminho1 aponte pra outro nó
                self.retornaPosicaoPalavra(palavra, caminho1)
        else: # seguindo o caminho 0
            if caminho0 == -1: # caso o caminho0 esteja vazio
                return -1
            elif isinstance(caminho0, int): # Caso o caminho aponte para a posição de uma palavra
                return caminho0
            else: # Caso o caminho0 aponte pra outro nó
                self.retornaPosicaoPalavra(palavra, caminho0)

    def retornaTraducoesPalavra(self, palavra: str):
        return Arquivo.retornaTraducoes(palavra)

    def retornaMorfologiaPalavra(self, palavra: str):
        return Arquivo.retornaMorfologia(palavra)

    def printaArvore(self, noBase: No):
        fesq = noBase.ponteiro0
        fdir = noBase.ponteiro1
        
        print("bit:", noBase.bitComparavel, '', end='')

        if isinstance(fesq, No):
            print('fesq:', fesq.bitComparavel, '', end='')
            if isinstance(fdir, No):
                print('fdir:', fdir.bitComparavel)
                self.printaArvore(fdir)
            elif fdir == -1:
                print('fdir: ')
            else:
                print('fdir:', Arquivo.lePosicaoArquivo(fdir).palavra)
            self.printaArvore(fesq)
        elif fesq == -1:
            print('fesq: ', end='')
            if isinstance(fdir, No):
                print('fdir:', fdir.bitComparavel)
                self.printaArvore(fdir)
            elif fdir == -1:
                print('fdir: ')
            else:
                print('fdir:', Arquivo.lePosicaoArquivo(fdir).palavra)
        else:
            print('fesq:', Arquivo.lePosicaoArquivo(fesq).palavra, '', end='')
            if isinstance(fdir, No):
                print('fdir:', fdir.bitComparavel)
                self.printaArvore(fdir)
            elif fdir == -1:
                print('fdir: ')
            else:
                print('fdir:', Arquivo.lePosicaoArquivo(fdir).palavra)
            
        