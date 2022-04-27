
entrada = input().split()

tamanho, intervalo = entrada
tamanho = int(tamanho)
intervalo = int(intervalo)

entrada = input().split()

valorPorKm, pedagio = entrada
valorPorKm = int(valorPorKm)
pedagio = int(pedagio)

totalPorKm = valorPorKm * tamanho
totalPedagio = (tamanho//intervalo) * pedagio

total = totalPorKm + totalPedagio

print(total)