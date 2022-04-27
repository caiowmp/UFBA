
entrada = input().split()

tamanho,distancia = entrada
tamanho = int(tamanho)
distancia = int(distancia)

saida = int(distancia%tamanho)

print(saida)