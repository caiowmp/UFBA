

try:
    #Cria o arquivo se ele não existir e abra-o no modo de gravação
    file = open("dados","w+")
except:
    print("Erro na criacao do arquivo \"dados\".")


file.close()