from operator import indexOf
from re import T
from registro import Registro
from arquivo import Arquivo

class ArvoreBp:

    def __init__ (self, GRAU_MINIMO_INDICE, FATOR_CONJSEQ):
        self.MAX_INDICES = GRAU_MINIMO_INDICE * 2 -1
        self.MIN_INDICES = GRAU_MINIMO_INDICE - 1 
        self.MAX_REG = FATOR_CONJSEQ * 2 - 1
        self.MIN_REG = FATOR_CONJSEQ - 1
        self.conjuntoSequencia = []
        try:
            self.conjuntoSequencia = Arquivo.leConjuntoSequencia()
        except:
            Arquivo.criaConjuntoSequencia()
        
    def insereRegistro (self, registro):
        if isinstance (registro, Registro):
            self.conjuntoSequencia = Arquivo.leConjuntoSequencia()
            #print(len(self.conjuntoSequencia))
            #verifica se a chave já está no arquivo
            if len(self.conjuntoSequencia) > 0:
                for reg in self.conjuntoSequencia:
                    if int(reg[0]) == registro.chave:
                        print('chave ja existente:', str(registro.chave))
                        return 
            #inserção do primeiro registro
            elif len(self.conjuntoSequencia) == 0:
                Arquivo.insereDadosConjuntoSequencia(repr(registro))
                print('insercao com sucesso:', registro.chave)
                return
            
            #inserção dos registros até o número max. Posso usar um arquivo para cada parte do conjunto sequencia ?
            anterior = '0'
            if len(self.conjuntoSequencia) < self.MAX_REG:
                #armazena o valor anterior do registro que vai entrar
                for reg in self.conjuntoSequencia:
                    if int(reg[0]) < registro.chave:
                        anterior = reg[0]
                idx = []
                #se ele não for o menor valor
                if anterior != '0':
                    #armazena o index do anterior
                    for reg in self.conjuntoSequencia:   
                        if reg[0] == anterior:
                            idx = self.conjuntoSequencia.index(reg)
                            break
                    #verifica se o anterior é o último e insere no final
                    if idx + 1 == len(self.conjuntoSequencia):
                        self.conjuntoSequencia.append(repr(registro).split(' '))
                        print('insercao com sucesso:', registro.chave)
                    #insere após o anterior
                    else:
                        self.conjuntoSequencia.insert(idx + 1, repr(registro).split(' '))
                        print('insercao com sucesso:', registro.chave)
                #insere no início
                else:
                    self.conjuntoSequencia.insert(0, repr(registro).split(' '))
                    print('insercao com sucesso:', registro.chave)

            #ecreve o conteúdo em uma variável
            conteudo = []
            for reg in self.conjuntoSequencia:
                #print(reg)
                conteudo.append(repr(Registro(int(reg[0]), reg[1], int(reg[2]))))

            #insere o conteúdo no arquivo
            Arquivo.insereDadosConjuntoSequencia(conteudo)

    def consultaRegistro (self, chave):
        pass

    def removeRegistro (self, chave):
        pass

    def imprimeArvore (self):
        pass

    def imprimeChaves (self):
        pass