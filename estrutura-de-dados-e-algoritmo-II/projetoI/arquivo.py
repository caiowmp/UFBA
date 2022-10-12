
from registro import Registro

class Arquivo:

    @classmethod
    def criaIndices (cls):
        file = open("projetoI\\indices","w+")
        file.close()

    @classmethod
    def criaConjuntoSequencia (cls):
        file = open("projetoI\\conjuntoSequencia","w+")
        file.close()

    @classmethod
    def insereDadosConjuntoSequencia (cls, registro):
        file = open('projetoI\\conjuntoSequencia','r')
        conteudo = file.readlines()
        conteudo.append(repr(registro))

        file = open('projetoI\\conjuntoSequencia','w')
        file.writelines(conteudo)
        file.close()

    @classmethod
    def insereDadosIndices (cls, registro):
        file = open('projetoI\\indices','r')
        conteudo = file.readlines()
        if isinstance(registro, Registro):
            conteudo.append("Chave: " + str(registro.chave))

        file = open('projetoI\\indices','w')
        file.writelines(conteudo)
        file.close()

    @classmethod
    def leConjuntoSequencia (cls):
        conjuntoSequencia = []
        with open('projetoI\\conjuntoSequencia') as arquivo:
            for linha in arquivo:
                linha = linha.split(' ')
                conjuntoSequencia.append(linha)
                
        return conjuntoSequencia

    @classmethod
    def leIndices (cls):
        pass