from registro import Registro
from arquivo import Arquivo

class ArvoreBp:

    def __init__ (self, GRAU_MINIMO_INDICE, FATOR_CONJSEQ):
        self.MAX_INDICES_NO = GRAU_MINIMO_INDICE * 2 -1
        self.MIN_INDICES_NO = GRAU_MINIMO_INDICE - 1 
        self.MAX_REG_NO = FATOR_CONJSEQ * 2 - 1
        self.MIN_REG_NO = FATOR_CONJSEQ - 1
        try:
            self.conjuntoSequencia = Arquivo.leConjuntoSequencia()
        except:
            Arquivo.criaConjuntoSequencia()
        
    def insereRegistro (self, registro):
        if isinstance (registro, Registro):
            self.conjuntoSequencia = Arquivo.leConjuntoSequencia()
            for reg in self.conjuntoSequencia:
                if int(reg[0]) == registro.chave:
                    print('chave ja existente:', str(registro.chave))
                    return 
                    

    def consultaRegistro (self, chave):
        pass

    def removeRegistro (self, chave):
        pass

    def imprimeArvore (self):
        pass

    def imprimeChaves (self):
        pass