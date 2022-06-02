# 						A busca de Leonidas

​															Autor: Micael Mota

​	Uma imagem pode ser representada nos computadores como uma matriz, onde cada posi¸c˜ao da
matriz possui um valor que representa um pixel da imagem.
​	Leonidas trabalha com reconhecimento facial e encontrou um problema nas imagens que ele usa
para processar. Ele identificou um pixel com intensidade fren´etica, quando esse pixel aparece na
imagem que ele est´a processando, o computador trava e ele precisa recome¸car do zero.
​	Leonidas pediu a sua ajuda para verificar se as imagens que ele est´a processando possuem algum
pixel fren´etico ou n˜ao. As imagens que ele trabalha tem tamanho 10x10.

### Entrada

​	A primeira linha da entrada cont´em um inteiro P, representando a intensidade do pixel fren´etico.
Cada uma das pr´oximas 10 linhas cont´em 10 inteiros X, representando a intensidade de cada pixel
naquela linha da imagem.

### Sa´ıda

​	Seu programa deve imprimir uma linha dizendo “sim”, caso a imagem tenha o pixel fren´etico, ou
“nao” caso contr´ario.

| Entrada                                                      | Saída |
| ------------------------------------------------------------ | ----- |
| 100<br/>14 13 35 9 38 27 11 27 8 21<br/>42 45 46 29 37 2 11 14 12 24<br/>45 33 15 48 19 43 10 47 31 47<br/>32 46 12 18 4 1 44 14 28 3<br/>37 19 48 32 49 34 33 9 49 46<br/>34 46 30 50 45 49 43 4 45 25<br/>3 28 21 14 46 24 14 39 40 43<br/>44 26 13 41 9 11 26 43 21 25<br/>41 5 20 20 6 16 18 50 19 15<br/>25 23 42 45 36 39 20 2 30 9 | nao   |

