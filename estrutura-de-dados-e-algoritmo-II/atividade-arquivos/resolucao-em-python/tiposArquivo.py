maiorTamArquivo = 10
maiorTamNome = 20


class DadosUsuario:
    def __init__(self):
        self.chave = 0
        self.nome = "dados"

    def info(self):
        return "chave = " + str(self.chave) + "\nnome = " + str(self.nome) + "\n"  


class Registro:
    def __init__(self):
        self.ocupado = True
        self.dados = DadosUsuario

    def __str__(self):
        return "ocupado = " + str(self.ocupado) + "\ndados = " + str(self.dados.info) + "\n"   
