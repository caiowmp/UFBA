class Registro:

    def __init__ (self, chave, nome, idade):
        self.chave = chave
        self.nome = nome
        self.idade = idade

    def __repr__ (self):
        return "Chave " + str(self.chave) + ", Nome " + str(self.nome) + ", Idade " + str(self.idade)