from tiposArquivo import *

try:
    file = open('dados','r')
    conteudo = file.readlines()
except:
    print("Erro na abertura do arquivo \"dados\" - Programa abortado")

r = Registro()

print("Informe uma chave: ")
r.dados.chave = int(input())

print("Entre com um nome: ")
r.dados.nome = input()

print("Entre com uma posicao do arquivo: ")
posarq = int(input())

print("Armazenando registro no arquivo ...")

r.ocupado = True
conteudo.append(str(r))

file = open('dados','w')

try:
    file.writelines(conteudo)
    print("Registro armazenado com sucesso")
except:
    print("Erro no armazenamento do registro")

file.close()