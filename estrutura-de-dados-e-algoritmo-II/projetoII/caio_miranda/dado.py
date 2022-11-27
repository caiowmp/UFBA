class Dado:

    def __init__(self, palavra, morfologia, traducoes):
        self.palavra = palavra
        self.morfologia = morfologia
        self.traducoes = traducoes
        
    def __str__(self):
        retorno = self.palavra + ',' + self.morfologia
        for i in self.traducoes:
            retorno += ',' + i
        retorno += ',\n'
        return retorno

    def retornaPalavraEmBinario(self):
        return ''.join(format(ord(i), 'b') for i in self.palavra)

    def __eq__(self, outro: object):
        return self.palavra == outro.palavra
        	