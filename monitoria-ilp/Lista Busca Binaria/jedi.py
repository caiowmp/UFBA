qtdPlanetas = int(input())

planetas = input().split()

qtdYoda = int(input())

planetasYoda = input().split()

matriz = []

for i in range(qtdPlanetas):
    linha = list(map(int,input().split()))
    matriz.append(linha)

posicao = 0
distancia = 0

for i in planetasYoda:
  inicio = 0 
  fim = qtdPlanetas - 1
  
  while inicio <= fim:
    meio = (inicio + fim)//2

    if planetas[meio] == i:
      distancia += matriz[meio][posicao]
      posicao = meio
      break
    elif planetas[meio] > i:
      fim = meio - 1
    elif planetas[meio] < i:
      inicio = meio + 1

print(distancia)