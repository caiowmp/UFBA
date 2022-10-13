
from registro import Registro

class Arquivo:

    @classmethod
    def criaIndices (cls):
        file = open("indices","w+")
        file.close()

    @classmethod
    def criaConjuntoSequencia (cls):
        file = open("conjuntoSequencia","w+")
        file.close()

    @classmethod
    def insereDadosConjuntoSequencia (cls, conteudo):

        file = open('conjuntoSequencia','w')
        file.writelines(conteudo)
        file.close()

    @classmethod
    def insereDadosIndices (cls, registro):
        file = open('indices','r')
        conteudo = file.readlines()
        if isinstance(registro, Registro):
            conteudo.append("Chave: " + str(registro.chave))

        file = open('indices','w')
        file.writelines(conteudo)
        file.close()

    @classmethod
    def leConjuntoSequencia (cls):
        conjuntoSequencia = []
        with open('conjuntoSequencia') as arquivo:
            for linha in arquivo:
                linha = linha.split(' ')
                conjuntoSequencia.append(linha)
                
        return conjuntoSequencia

    @classmethod
    def leIndices (cls):
        pass