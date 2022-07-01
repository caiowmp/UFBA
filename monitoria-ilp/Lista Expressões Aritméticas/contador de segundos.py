
entrada = input()

entrada = int(entrada)

# equivale a horas = int(entrada/3600)
horas = entrada//3600
resto = entrada%3600

#equivale a minutos = int(resto/60)
minutos = resto//60
resto = resto%60

segundos = resto


print(horas ,"h ",minutos,"m ",segundos,"s",sep="")
# ou print(str(horas) + "h " + str(minutos) + "m " + str(segundos) + "s")
