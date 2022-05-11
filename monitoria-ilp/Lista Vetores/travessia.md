# 									A grande travessia 

Enquanto estava de férias nas montanhas, você percebeu que uma fam lia de ı́lia de sapos estava tentando atravessar um rio, pulando por um caminho de pedras que ia de um lado ao outro. Você percebeu que cada sapo tinha um tamanho de pulo diferente, e por isso não precisavam necessariamente passar por todas as pedras. Por exemplo, se um sapo tivesse tamanho de pulo igual a 2, ele poderia pular da primeira pedra para terceira pedra, depois para a quinta, até chegar ao outro lado do rio. Sabendo disso, você ficou curioso para saber por quais pedras os sapos passaram. 

## Entrada

 A primeira linha consiste em um inteiro ‘S’ (1 <= S <= 50), o número de sapos na fam lia ı́lia e um inteiro ‘N’ (1 <= N <= 100) , o número de pedras no caminho. As próximas ‘S’ linhas contém um valor ‘P’ (1 <= P <= 50) cada, correspondente ao tamanho do pulo de cada sapo. Saiba que cada sapo começa na primeira pedra e que as pedras estão numeradas de 0 a N-1. 

## Saída

 Você deve imprimir em uma única linha o estado de todas as pedras (pedra 0 até a pedra N-1) do caminho, imprima 0 caso a pedra não tenha sido pisada por nenhum sapo, ou 1 caso algum sapo tenha passado por aquela pedra. Imprima espaço entre as pedras

| Entrada                   | Saída               |
| ------------------------- | ------------------- |
| 3 10<br />2<br />5<br />4 | 1 0 1 0 1 1 1 0 1 0 |
| 1 5 <br />2               | 1 0 1 0 1           |

