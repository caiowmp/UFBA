# 											SRT Intergalática

​																							Autora: Laila Mota

​	Os vogons estão responsáveis por realizar a destruição de todos os planetas que estiverem no caminho
da nova SRT (Spaceship Rapid Transit), que será feita para melhorar o tráfego de naves pelo espaço.
​	Como eles não são conhecidos por sua inteligência, os vogons receberam apenas uma tabela com os
planetas renomeados e ordenados em números de 1 a N (seus novos identificadores) e, ao lado do
identificador de cada planeta, um outro número referente ao grau de urgência da demolição daquele
planeta (quanto maior, mais urgente). Os ratos, os seres mais inteligentes do Universo, pediram para você
criar um programa que ordene os planetas por prioridade de demolição, mantendo o número de identificação
deles lado a lado, de forma que os vogons não destruam o planeta errado antes da hora.

### Entrada

​	A primeira linha da entrada consiste de um inteiro ‘N’ (1 <= N <= 50), o número de planetas
contidos na tabela. Em cada uma das ‘N’ linhas seguintes teremos dois inteiros: os números de
identificação de cada planeta I (1 <= I <= N); e o grau de urgência R (1 <= R <= 500) da demolição
daquele planeta.

### Saída

​	Seu programa deve imprimir os planetas reordenados por grau de urgência da demolição, do
mais urgente para o menos urgente. 

| Entrada                                            | Saída                                        |
| -------------------------------------------------- | -------------------------------------------- |
| 5<br/>1 220<br/>2 43<br/>3 333<br/>4 436<br/>5 375 | 4 436<br/>5 375<br/>3 333<br/>1 220<br/>2 43 |
| 2<br/>1 475<br/>2 117                              | 1 475<br/>2 117                              |

