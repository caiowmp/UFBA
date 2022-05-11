# 					Dr. Strange e as Multidimensões

 Não é novidade para ninguém que o Dr. Strange, o famoso mago da Marvel, tem a incrível habilidade de viajar entre dimensões. Mas poucos sabem que realizar tal feito não é tão fácil quanto parece.

 Primeiro, Dr. Strange precisa pensar na dimensão que ele quer chegar. Para isso, ele pensa em um número inteiro ‘N’ >= 2, indicando o número da dimensão de destino. Por exemplo, se Dr. Strange deseja viajar para a sexta dimensão, ‘N’ = 6, significa que cada ponto dessa dimensão pode ser especificado por uma sequência de seis números s = (n1,n2,n3,n4,n5,n6). Assim, se Dr. Strange deseja viajar para a ‘N’-ésima dimensão, cada ponto dessa dimensão pode ser especificado por uma sequência de ‘N’ números s = (n1, n2, …, nn), onde ni é um número real qualquer, para 1 <= i <= n. 

 O próximo passo é mais complicado. Escolhida a dimensão, Dr. Strange escolhe o ponto dessa dimensão para onde ele deseja viajar, denotado D. A questão é que Dr. Strange não pode viajar diretamente para D, primeiro ele deve viajar para um ponto intermediário, e de lá viajar para D. Essa operação de viajar para um ponto e depois para o seu destino pode ser especificada como uma soma de sequências na mesma dimensão, ou seja, dado o destino D e duas sequências ‘u’ e ‘v’, todos na dimensão ‘N’, sua tarefa é descobrir se a soma das duas sequências irá levar Dr. Strange para o ponto D. A soma de duas sequências é definida da seguinte forma: seja u = (a1, a2, …, an) e v = (b1, b2, …, bn), u + v = (a1+b1, a2+b2, …, an + bn). 

## Entrada:

 A primeira linha da entrada contém um inteiro ‘N’ (1 ≤ ‘N’ ≤ 1000). Indicando a dimensão para a qual Dr. Strange deseja viajar. As próximas três linhas indicam, respectivamente, os ‘N’ números inteiros de cada uma das sequências u, v, e do ponto D. 

## Saída: 

 A saída é composta de uma única linha com as possíveis respostas sem aspas: “OK”, se Dr. Strange consegue viajar para D, dadas as sequências u e v, e “NOPE :(”, caso contrário.

| Entrada                                   | Saída   |
| ----------------------------------------- | ------- |
| 4<br />1 2 3 4<br />4 7 9 1<br />5 9 12 5 | OK      |
| 3<br />1 2 4<br />1 56 22<br />1 2 4      | NOPE :( |

