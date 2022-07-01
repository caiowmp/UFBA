inicialList = []

# recebe as entradas separadas 
# map converte a entrada que vem em formato string em int
value = map(int, input().split())

# joga as entradas na lista
for i in value:
    inicialList.append(i)

#copia a inicialList para a sortedList
sortedList = inicialList.copy()
#ordena a sortedList
sortedList.sort()

#SAÍDA:
for i in sortedList:
    print(i)

print()

for i in inicialList:
    print(i)
    