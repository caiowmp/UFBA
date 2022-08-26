from tiposArquivo import *

print("Criando arquivo \"dados\"...")

try:
    #Cria o arquivo se ele não existir e abra-o no modo de gravação
    file = open("dados","w+")
    print("Arquivo \"dados\" criado com sucesso.")
except:
    print("Erro na criacao do arquivo \"dados\".")

print("Inicializando o arquivo ...")


r = Registro()
r.ocupado = False

file.write(str(r))

file.close()