from dado import Dado

# Documento para manipulação de arquivos

class Arquivo:
    
    @classmethod
    def leArquivo(cls):
        conteudo = []
        try: # tenta ler o arquivo
            with open("arquivo.dat") as arquivo:
                for linha in arquivo:
                    palavra = linha.split(',')[0]
                    morfologia = linha.split(',')[1]
                    traducoes = linha.split(',')[2:]
                    conteudo.append(Dado(palavra, morfologia, traducoes))
        except: # Cria o arquivo
            arquivo = open("arquivo.dat","wb")
            arquivo.close()                   
        return conteudo

    @classmethod
    def escreveArquivo(cls, dado: Dado):
        arquivo = open("arquivo.dat","ab+")
        arquivo.write(dado.__str__().encode("utf-8"))
        arquivo.close()

    @classmethod
    def lePosicaoArquivo(cls, posicao: int):
        with open("arquivo.dat") as arquivo:
            contador = 0
            for linha in arquivo:
                if contador == posicao:
                    palavra = linha.split(',')[0]
                    morfologia = linha.split(',')[1]
                    traducoes = linha.split(',')[2:]
                    return Dado(palavra, morfologia, traducoes)    
                contador +=1

    @classmethod
    def verficaSePalavraJaExiste(cls, palavra: str):
        conteudo = Arquivo.leArquivo()
        for i in conteudo:
            if i.palavra == palavra:
                return True

    @classmethod
    def retornaPalavrasOrdemCrescente(cls):
        arquivo = Arquivo.leArquivo() 
        if len(arquivo) == 0:
            return ''
        palavras = []
        palavrasEmBinario = []       
        for i in arquivo:
            palavras.append(i.palavra)
            palavrasEmBinario.append(i.retornaPalavraEmBinario())
        for i in range(len(palavrasEmBinario)-1):
            for j in range(i+1, len(palavrasEmBinario)):
                if len(palavrasEmBinario[i]) > len(palavrasEmBinario[j]): # caso o tamaho de i seja maior q o de j
                    auxB = palavrasEmBinario[i]
                    palavrasEmBinario[i] = palavrasEmBinario[j]
                    palavrasEmBinario[j] = auxB
                    aux = palavras[i]
                    palavras[i] = palavras[j]
                    palavras[j] = aux
                elif len(palavrasEmBinario[i]) < len(palavrasEmBinario[j]): # caso o tamanho de i seja menor q o de j
                    continue
                else:
                    if palavras[i] > palavras[j]:
                        auxB = palavrasEmBinario[i]
                        palavrasEmBinario[i] = palavrasEmBinario[j]
                        palavrasEmBinario[j] = auxB
                        aux = palavras[i]
                        palavras[i] = palavras[j]
                        palavras[j] = aux
        return palavras

    @classmethod
    def retornaPalavrasOrdemDecrescente(cls):
        arquivo = Arquivo.leArquivo() 
        if len(arquivo) == 0:
            return ''
        palavras = []
        palavrasEmBinario = []       
        for i in arquivo:
            palavras.append(i.palavra)
            palavrasEmBinario.append(i.retornaPalavraEmBinario())
        for i in range(len(palavrasEmBinario)-1):
            for j in range(i+1, len(palavrasEmBinario)):
                if len(palavrasEmBinario[i]) < len(palavrasEmBinario[j]): # caso o tamaho de i seja maior q o de j
                    auxB = palavrasEmBinario[i]
                    palavrasEmBinario[i] = palavrasEmBinario[j]
                    palavrasEmBinario[j] = auxB
                    aux = palavras[i]
                    palavras[i] = palavras[j]
                    palavras[j] = aux
                elif len(palavrasEmBinario[i]) > len(palavrasEmBinario[j]): # caso o tamanho de i seja menor q o de j
                    continue
                else:
                    if palavras[i] < palavras[j]:
                        auxB = palavrasEmBinario[i]
                        palavrasEmBinario[i] = palavrasEmBinario[j]
                        palavrasEmBinario[j] = auxB
                        aux = palavras[i]
                        palavras[i] = palavras[j]
                        palavras[j] = aux
        return palavras

    @classmethod
    def retornaPalavraEmBinario(cls, palavra: str):
        return ''.join(format(ord(i), 'b') for i in palavra)

    @classmethod
    def retornaTraducoes(cls, palavra: str):
        dados = Arquivo.leArquivo()
        for i in dados:
            if i.palavra == palavra:
                return i.traducoes
        print('palavra inexistente no dicionario:', palavra)
        return ''

    @classmethod
    def retornaPalavrasOrdemDecrescenteMorfologia(cls, morfologia: str):
        arquivo = Arquivo.leArquivo() 
        if len(arquivo) == 0:
            return ''
        palavras = []
        palavrasEmBinario = []       
        for i in arquivo:
            if i.morfologia == morfologia:
                palavras.append(i.palavra)
                palavrasEmBinario.append(i.retornaPalavraEmBinario())
        for i in range(len(palavrasEmBinario)-1):
            for j in range(i+1, len(palavrasEmBinario)):
                if len(palavrasEmBinario[i]) < len(palavrasEmBinario[j]): # caso o tamaho de i seja maior q o de j
                    auxB = palavrasEmBinario[i]
                    palavrasEmBinario[i] = palavrasEmBinario[j]
                    palavrasEmBinario[j] = auxB
                    aux = palavras[i]
                    palavras[i] = palavras[j]
                    palavras[j] = aux
                elif len(palavrasEmBinario[i]) > len(palavrasEmBinario[j]): # caso o tamanho de i seja menor q o de j
                    continue
                else:
                    if palavras[i] < palavras[j]:
                        auxB = palavrasEmBinario[i]
                        palavrasEmBinario[i] = palavrasEmBinario[j]
                        palavrasEmBinario[j] = auxB
                        aux = palavras[i]
                        palavras[i] = palavras[j]
                        palavras[j] = aux
        return palavras

    @classmethod
    def retornaPalavrasOrdemCrescenteMorfologia(cls, morfologia: str):
        arquivo = Arquivo.leArquivo() 
        if len(arquivo) == 0:
            return ''
        palavras = []
        palavrasEmBinario = []       
        for i in arquivo:
            if i.morfologia == morfologia:
                palavras.append(i.palavra)
                palavrasEmBinario.append(i.retornaPalavraEmBinario())
        for i in range(len(palavrasEmBinario)-1):
            for j in range(i+1, len(palavrasEmBinario)):
                if len(palavrasEmBinario[i]) > len(palavrasEmBinario[j]): # caso o tamaho de i seja maior q o de j
                    auxB = palavrasEmBinario[i]
                    palavrasEmBinario[i] = palavrasEmBinario[j]
                    palavrasEmBinario[j] = auxB
                    aux = palavras[i]
                    palavras[i] = palavras[j]
                    palavras[j] = aux
                elif len(palavrasEmBinario[i]) < len(palavrasEmBinario[j]): # caso o tamanho de i seja menor q o de j
                    continue
                else:
                    if palavras[i] > palavras[j]:
                        auxB = palavrasEmBinario[i]
                        palavrasEmBinario[i] = palavrasEmBinario[j]
                        palavrasEmBinario[j] = auxB
                        aux = palavras[i]
                        palavras[i] = palavras[j]
                        palavras[j] = aux
        return palavras

    @classmethod
    def retornaMorfologia(cls, palavra: str):
        dados = Arquivo.leArquivo()
        for i in dados:
            if i.palavra == palavra:
                return i.morfologia
        return ''