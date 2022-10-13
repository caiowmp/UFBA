class Registro:

    def __init__ (self, chave: int, nome, idade: int):
        self.chave = chave
        self.nome = nome
        self.idade = idade

    def __repr__ (self):
        return str(self.chave) + " " + self.nome+ " " + str(self.idade) + ' \n'