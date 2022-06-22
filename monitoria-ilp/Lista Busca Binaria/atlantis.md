# 										Atlantis

​																		Autor: Pedro Vidal

​	Você é um explorador que descobriu a cidade de Atlantis pouco antes
dela afundar e conseguiu presenciar e fotografar os últimos momentos da
cidade do seu helicóptero. Utilizando essa foto, você conseguiu determinar a
altura de cada parte da cidade em metros no momento 0, ou seja, antes da
água inundar a cidade. A cada hora, a água subia 1 metro. Você deseja saber
um pouco mais sobre os últimos momentos dessa grande civilização e por isso
deseja saber quantas partes da cidade foram inundadas dado a foto original, e
quantas horas se passaram desde o momento 0.

### Entrada

​	A primeira linha da entrada contêm dois inteiros, ‘N’ e ‘M’ (1 <= N,M
<= 300), que representam a largura e o comprimento da foto original. Cada
uma das próximas ‘N’ linhas contêm ‘M’ inteiros ‘A’ (1 <= A <= 1000), que
representam a altura de cada parte da cidade no momento 0. A próxima linha
contêm um inteiro ‘Q’ (1 <= Q <= 10000), o número de consultas que você
irá fazer. A linha seguinte contêm ‘Q’ inteiros ‘H’ (1 <= H <= 1000), que
representam o número de horas que se passaram desde o instante 0, para
cada uma das ‘Q’ consultas.

### Saída

​	Para cada consulta você deve imprimir um número inteiro, que é o
número de partes da cidade que já foram inundadas. Ou seja, basta verificar
na foto (mapa – matriz) o número de partes da cidade que são menores ou
iguais ao tempo ‘H’ dado para uma certa consulta ‘Q’, já que a cada hora o
nível do mar se eleva em 1 metro.

| Entrada                                                      | Saída           |
| ------------------------------------------------------------ | --------------- |
| 4 4<br/>1 1 2 2<br/>3 5 5 1<br/>2 3 6 5<br/>1 1 1 1<br/>3<br/>1 7 4 | 7<br/>16<br/>12 |

