# 									Quill é muito organizado!

​																					Autor: Iure Vieira Guimarães

​	No universo de Guardiões da Galáxia é possível
passear por vários planetas muito rapidamente através
de pontos de salto que existem nas galáxias. Peter
Quill, não sabe exatamente por quais planetas a
tripulação passou nos últimos anos, mas ele tem
armazenado em um vetor quais foram estes. Para não
demorar procurando, ele pediu que você
desenvolvesse um programa que informe, de forma
bastante rápida, se eles já visitaram determinado
planeta. A tripulação trata os planetas como números
inteiros, pois Groot nunca consegue lembrar dos nomes.

### Tarefa

​	Dado um vetor ordenado com os números dos planetas que já foram visitados, você deve
informar a posição do planeta no vetor de Quill. Isso confirmará que o planeta já foi visitado e ainda
provará para Gamora que Quill é organizado.

### Entrada

​	Será dado um inteiro ‘N’ (1 <= ’N’ <= 50000), que representa a quantidade de planetas que já
foram visitados pela tripulação. Na próxima linha serão dados os códigos dos planetas visitados. Na
linha seguinte serão informados vários inteiros ‘P’ (1 <= ‘P’ <= 50000) que representam os números
dos planetas que precisam ser verificados. Caso o número seja 0, você deverá finalizar o programa.

### Saída

​	Para cada planeta que for verificado, você deverá imprimir uma linha. Caso o planeta já
tenha sido visitado, você deverá informar o índice desse planeta no vetor. Caso não tenha sido
visitado, você deverá imprimir "Nao foi visitado ainda.", sem aspas.

| Entrada                                                      | Saída                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 15<br/>1 3 7 18 19 23 36 42 52 68 192 202 203 600 723<br/>7 192 3 36 702 600 0 | 2<br/>10<br/>1<br/>6<br/>Nao foi visitado ainda.<br/>13      |
| 8<br/>5 14 19 33 42 101 110 919<br/>718 110 919 4 19 0       | Nao foi visitado ainda.<br/>6<br/>7<br/>Nao foi visitado ainda.<br/>2 |

