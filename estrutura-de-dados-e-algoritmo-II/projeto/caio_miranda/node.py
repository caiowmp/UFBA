from enum import Enum
from subprocess import SubprocessError

class Response(Enum):
    SUCESSO = 1
    FALHA = 2
    MANUTENCAO = 3

class Node:
    def __init__(self, grau_minimo_indice, fator_conjseq):
        self.eh_folha = True
        self.chaves = []
        self.ponteiros = []
        self.dados = []
        self.grau_minimo_indice = grau_minimo_indice
        self.fator_conjseq = fator_conjseq

    def __str__(self):
        return ' '.join(self.chaves)

    def fazer_dict(self):
        node_list = self.pegar_nodes()
        node_dict = {}
        for i, node in enumerate(node_list):
            novo_dict = {
                'chaves': node.chaves,
                'dados': node.dados,
                'eh_folha': node.eh_folha
            }
            ponteiros = []
            for ponteiro in node.ponteiros:
                if ponteiro is None:
                    continue
                ponteiros.append(node_list.index(ponteiro) + 1)
            novo_dict['ponteiros'] = ponteiros
            node_dict[i] = novo_dict
        return node_dict

    def dividir(self):
        direita = Node(self.grau_minimo_indice, self.fator_conjseq)
        esquerda = Node(self.grau_minimo_indice, self.fator_conjseq)
        meio = self.fator_conjseq

        esquerda.chaves = self.chaves[:meio]
        esquerda.dados = self.dados[:meio]
        esquerda.ponteiros = self.ponteiros[:meio]

        direita.chaves = self.chaves[meio:]
        direita.dados = self.dados[meio:]
        direita.ponteiros = self.ponteiros[meio:]

        self.chaves = [esquerda.chaves[-1]]
        self.ponteiros = [esquerda, direita]
        self.dados = []
        self.eh_folha = False

    def buscar(self, chave):
        if chave in self.chaves:
            index = self.chaves.index(chave)
            if self.eh_folha:
                return self.dados[index]
            if len(self.ponteiros) - 1 >= index:
                return self.ponteiros[index].buscar(chave)
            return False
        elif self.eh_folha:
            return None

        for i, c in enumerate(self.chaves):
            if c > chave:
                return self.ponteiros[i].buscar(chave)
            elif i + 1 == len(self.chaves) == len(self.ponteiros):
                return self.ponteiros[i+1].buscar(chave)
        return None

    def adiciona(self, nova_chave, novo_dado):
        if not self.chaves:
            self.chaves.append(nova_chave)
            self.dados.append(novo_dado)
            return
        
        for i, chave in enumerate(self.chaves):
            if nova_chave < chave:
                self.chaves.insert(i, nova_chave)
                self.dados.insert(i, novo_dado)
                return
            elif i + 1 == len(self.chaves):
                self.chaves.append(nova_chave)
                self.dados.append(novo_dado)
                return

# 1 = Sucesso; 2 = Chave não encontrada, 3 = Requer redistribuição
    def remover(self, target):
        if self.eh_folha:
            if target not in self.chaves:
                return Response.FALHA
            index = self.chaves.index(target)
            self.chaves.pop(index)
            if len(self.chaves) + 1 >= self.fator_conjseq:
                return Response.SUCESSO
            return Response.MANUTENCAO
        
        for index, chave in enumerate(self.chaves):
            if chave >= target:
                response = self.ponteiros[index].remover(target)
                break
            elif index + 1 == len(self.chaves):
                response = self.ponteiros[index+1].remover(target)
                index += 1
                break

        if response != Response.MANUTENCAO:
            return response

        eh_emprestavel = lambda x: x.eh_folha and len(x.chaves) >= self.fator_conjseq
        if index > 0 and eh_emprestavel(self.ponteiros[index - 1]):
            chave_emprestada = self.ponteiros[index - 1].chaves.pop(-1)
            dado_emprestado = self.ponteiros[index - 1].dados.pop(-1)
            self.ponteiros[index].chaves.insert(0, chave_emprestada)
            self.ponteiros[index].dados.insert(0, dado_emprestado)
            self.chaves[index] = chave_emprestada
            return Response.SUCESSO
        
        if index + 1 < len(self.chaves) and eh_emprestavel(self.ponteiros[index + 1]):
            chave_emprestada = self.ponteiros[index + 1].chaves.pop(0)
            dado_emprestado = self.ponteiros[index + 1].dados.pop(0)
            self.ponteiros[index].chaves.insert(-1, chave_emprestada)
            self.ponteiros[index].dados.insert(-1, dado_emprestado)
            self.chaves[index] = chave_emprestada
            return Response.SUCESSO

        if len(self.ponteiros[index - 1].chaves) + len(self.ponteiros[index].chaves) <= self.fator_conjseq * 2 - 1:
            self.ponteiros[index - 1].chaves.extend(self.ponteiros[index].chaves)
            self.ponteiros[index - 1].dados.extend(self.ponteiros[index].dados)
            self.ponteiros.pop(index)
            self.chaves[index] = self.ponteiros[index].chaves[0]
            self.chaves.pop(index - 1)
            return Response.SUCESSO

        self.ponteiros[index + 1].chaves = self.ponteiros[index].chaves + self.ponteiros[index + 1].chaves
        self.ponteiros[index + 1].dados = self.ponteiros[index].dados + self.ponteiros[index + 1].dados
        self.ponteiros.pop(index)
        self.chaves[index] = self.ponteiros[index].chaves[0]
        self.chaves.pop(index + 1)
        return Response.SUCESSO

    
    def pegar_folhas(self):
        nodes = self.pegar_nodes()
        nodes = [node for node in nodes if node.eh_folha]
        chaves = []
        for node in nodes:
            chaves.extend(node.chaves)
        chaves.sort()
        return chaves

    def pegar_nodes(self):
        nodes = [self]

        for node in self.ponteiros:
            if node is None:
                continue
            nodes += node.pegar_nodes()

        return nodes
