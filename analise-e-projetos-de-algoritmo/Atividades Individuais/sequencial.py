from itertools import permutations

tamanho = int(input())

# criando o vetor para permutar
vetor = [ 1 * x for x in range(tamanho)]
print(vetor)

perm = permutations(vetor)

# Imprime as permutações
for i in list(perm):
    printa = True

    # verifica se existe algum valor na casa de seu valor
    for j in range(tamanho):
        if i[j] == j:
            printa = False

    if printa == True:
        print(i) 