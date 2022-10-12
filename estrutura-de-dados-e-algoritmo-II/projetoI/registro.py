class Registro:

    def __init__ (self, chave, nome, idade):
        self.chave = chave
        self.nome = nome
        self.idade = idade

    def __repr__ (self):
        return str(self.chave) + " " + str(self.nome) + " " + str(self.idade) + ' \n'