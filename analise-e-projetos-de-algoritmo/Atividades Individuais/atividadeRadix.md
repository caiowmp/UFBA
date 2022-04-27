# Atividade:

    Apresente o passo a passo do algoritmo de ordenação radix para as palavras: COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX.

# Resposta:

## Passo 1:

    Considerando o array dado para ser ordenado. Primeiro, por se tratar de strings, vamos descobrir qual o maior número de dígitos que uma string do array tem.

## Passo 2:

    Achado o maior número de dígitos possível, chamaremos a função bubbleSort para ordenar o array no intervalo dado, começando do dígito menos significativo e parando no mais signifcativo.

## Passo 3:

    Dentro da função bubbleSorte, comparamos cada dígito do intervalo dado e trocamos as palavras mediante a condição (o menor sempre na frente - ordem crescente).