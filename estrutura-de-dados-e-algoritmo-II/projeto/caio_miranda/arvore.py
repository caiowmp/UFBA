from node import Node


class Arvore:
    def __init__(self, grau_minimo_indice, fator_conjseq):
        self.raiz = Node(grau_minimo_indice, fator_conjseq)
        self.grau_minimo_indice = grau_minimo_indice
        self.fator_conjseq = fator_conjseq

    def dividir(self, pai, filho):
        filho.dividir()

        if pai is not None:
            for i, chave in enumerate(pai.chaves):
                if filho.chaves[0] < chave:
                    pai.chaves.insert(i, filho.chaves[0])
                    pai.ponteiros.pop(i)
                    pai.ponteiros.insert(i, filho.ponteiros[0])
                    pai.ponteiros.insert(i + 1, filho.ponteiros[1])
                    break
                elif i + 1 == len(pai.chaves):
                    pai.chaves.append(filho.chaves[0])
                    pai.ponteiros.pop(i + 1)
                    pai.ponteiros.extend(filho.ponteiros)
                    break

    def inserir(self, nova_chave, novo_dado):
        pai = None
        filho = self.raiz

        while not filho.eh_folha:
            if len(filho.chaves) == self.grau_minimo_indice * 2 - 1:
                direita = Node(self.grau_minimo_indice, self.fator_conjseq)
                esquerda = Node(self.grau_minimo_indice, self.fator_conjseq)
                meio = self.grau_minimo_indice

                esquerda.chaves = filho.chaves[: meio - 1]
                esquerda.dados = filho.dados[: meio - 1]
                esquerda.ponteiros = filho.ponteiros[:meio]
                esquerda.eh_folha = False

                direita.chaves = filho.chaves[meio:]
                direita.dados = filho.dados[meio:]
                direita.ponteiros = filho.ponteiros[meio:]
                direita.eh_folha = False

                filho.chaves = [filho.chaves[meio-1]]
                filho.ponteiros = [esquerda, direita]
                filho.dados = []
                filho.eh_folha = False

            pai = filho

            for i, chave in enumerate(pai.chaves):
                if nova_chave <= chave:
                    filho = pai.ponteiros[i]
                    break
                elif i + 1 == len(pai.chaves):
                    filho = pai.ponteiros[-1]
                    break

        if nova_chave in filho.chaves:
            return False

        if len(filho.chaves) == (self.fator_conjseq * 2) - 1:
            self.dividir(pai, filho)
            while not filho.eh_folha:
                for i, chave in enumerate(filho.chaves):
                    if nova_chave <= chave:
                        filho = filho.ponteiros[i]
                        break
                    elif i + 1 == len(filho.chaves):
                        filho = filho.ponteiros[i + 1]
                        break

        filho.adiciona(nova_chave, novo_dado)
        return True

    def buscar(self, chave):
        return self.raiz.buscar(chave)

    def imprimir(self):
        node_dict = self.raiz.fazer_dict()
        if not list(node_dict.values()):
            return
        for l, item in node_dict.items():
            print(f"No: {l+1}: ", end="")
            for i, chave in enumerate(item["chaves"]):
                if not item["eh_folha"]:
                    print(f"apontador: {item['ponteiros'][i]}", end=" ")
                print(f"chave: {chave}", end=" ")
            if not item["eh_folha"] and i + 1 < len(item["ponteiros"]):
                print(f"apontador: {item['ponteiros'][i+1]}", end=" ")
            if(l + 1 < len(node_dict.items())):
                print("")

    def remover(self, target):
        return self.raiz.remover(target)

    def pegar_folhas(self):
        return self.raiz.pegar_folhas()
