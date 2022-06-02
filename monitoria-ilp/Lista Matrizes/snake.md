# 												Snake

​																				Autor: Ubiratan Neto

​	Snake, a cobra, realiza todos os dias um percurso que pode ser representado por uma matriz
N x M . Ela começa no ponto (0, 0) e termina no ponto (N − 1, M − 1). Snake sempre se movimenta
da seguinte forma: na primeira linha da matriz que representa o caminho, ela parte da
esquerda para a direita. Na próxima linha, Snake percorre da direita para a esquerda. Na
linha seguinte percorre da esquerda para a direita e assim sucessivamente.
​	Durante o percurso, Snake pode coletar ovos para comer, caso ela passe por uma posição
que contenha algum (Snake ama ovos de aves, e ela não gosta de comer antes de chegar no seu
local de destino). Além disso, em alguns locais, as aves da região, enfurecidas por terem seus ovos
sendo roubados, armaram emboscadas para Snake, deixando-a imobilizada por alguns segundos,
tempo suficiente para recuperar alguns dos ovos roubados.
​	Sua tarefa é descobrir, dada a matriz do caminho que Snake percorre naquele dia, da forma
dita acima, as posições que contém ovos e as posições onde existem armadilhas, diga quantos ovos
Snake terá quando chegar em seu destino naquele dia. Como o destino de Snake é o ponto (N −
1, M − 1), é garantido que N é sempre ı́mpar.

### Entrada

​	A primeira linha da entrada possui 2 inteiros ‘N’ e ‘M’ (1 <= N, M <= 100), indicando as
dimensões da matriz que representa o percurso de Snake. Nas próximas ‘N’ linhas haverão ‘M’
inteiros ‘X’ (-2 <= ‘X’ <= 2), separados por um espaço em branco, representando a matriz. Para
cada elemento ‘X’ da matriz, caso ele seja positivo significa que existem ‘X’ ovos naquela posição, e
​	Snake coletará todos. Caso ‘X’ seja negativo, sabe-se que naquela posição existe uma armadilha
das aves, e que Snake perderá ‘X’ ovos ao passar por lá. Caso ‘X’ seja 0 nada acontece e Snake
pode passar tranquilamente pelo local.

### Saída

​	A saı́da deve conter um número inteiro: o número de ovos que Snake terá consigo ao chegar
em seu destino.

| Entrada                                   | Saída |
| ----------------------------------------- | ----- |
| 3 4<br/>0 0 2 1<br/>0 0 -1 0<br/>1 0 -2 1 | 2     |
| 1 3<br/>1 0 -1                            | 0     |

