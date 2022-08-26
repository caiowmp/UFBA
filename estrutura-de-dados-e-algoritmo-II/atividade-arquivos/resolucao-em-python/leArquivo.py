from tiposArquivo import *

try:
    file = open('dados','r')
except:
    print("Erro na abertura do arquivo \"dados\" - Programa abortado")

r = Registro()

for i in range(maiorTamArquivo):
    file.readlines()

    if r.ocupado == True:
        print("Ocupado: sim\nChave: ", r.dados.chave, "\nNome: ", r.dados.nome)
    else:
        print("Ocupado: não")

file.close()