pressao_erupcao = int(input())

resultado = "O Havai pode dormir tranquilo"

entrada = 1

while entrada != 0: 
    entrada = int(input())

    if entrada > pressao_erupcao:
        resultado = "ALARME"
    
print(resultado)