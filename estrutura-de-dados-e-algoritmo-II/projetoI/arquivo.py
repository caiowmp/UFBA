
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
    def insereDadosConjuntoSequencia (cls, registro):
        file = open('conjuntoSequencia','r')
        conteudo = file.readlines()
        '''if isinstance(registro, Registro):
            conteudo.append("Chave " + str(registro.chave) + ", ")
            conteudo.append("Nome " + str(registro.nome) + ", ")
            conteudo.append("Idade " + str(registro.idade) + '\n')'''
        conteudo.append(repr(registro))

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
        pass

    @classmethod
    def leIndices (cls):
        pass