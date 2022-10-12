'''Por favor, dê enter a cada linha inserida'''

from registro import Registro
from arvoreBp import ArvoreBp

GRAU_MINIMO_INDICE = 3
FATOR_CONJSEQ = 2

#cria a arvore b+
arvore = ArvoreBp(GRAU_MINIMO_INDICE, FATOR_CONJSEQ)

while True:

    operacao = input()

    #insere registro
    if operacao == 'i':
        chave = int(input())
        nome = input()
        idade = int(input())
        arvore.insereRegistro(Registro(chave, nome, idade))
    #consulta registro
    elif operacao == 'c':
        chave = int(input())
        arvore.consultaRegistro(chave)
    #remove registro
    elif operacao == 'r':
        chave = int(input())
        arvore.removeRegistro(chave)
    #imprime arvore
    elif operacao == 'p':
        arvore.imprimeArvore()
    #imprime chaves em ordem crescente
    elif operacao == 'o':
        arvore.imprimeChaves()
    #para o programa
    elif operacao == 'e':
        break
    
