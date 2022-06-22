# 												Mestre Jedi

​	Há muito tempo atrás, em uma galáxia
muito muito distante, o império do mal estava
construindo uma força, destruindo tudo em seu
caminho. Mas os rebeldes não têm medo, ao
lado negro da força eles nunca vão se juntar.
Uma esperança ainda existe. Yoda vai nos
levar para a luz, é hora de levantar e lutar.
​	Ele voa entre as estrelas na velocidade da luz para ensinar os jovens Jedi. Parabéns, você
nível subiu! Agora você pode mestre Jedi ser. Ajudar Mestre Yoda a percorrer a galáxia você precisa.

### Entrada

​	Na primeira linha será dado um inteiro ‘N’ (1 <= ‘N’ <= 1000) que representa a quantidade de
planetas na galáxia. Na próxima linha serão dados os códigos dos ‘N’ planetas, em ordem
alfabética, sendo cada código com 6 caracteres entre letras maiúsculas. Na próxima linha, será dado
um inteiro ‘X’ (1 <= ‘X’ <= 1000), a quantidade de planetas para os quais Yoda irá para treinar os
jovens Jedi. Nas próximas ‘X’ linhas serão dados os códigos dos planetas e Yoda irá percorrê-los na
ordem dada. Por fim, será dada uma matriz de distância de dimensões ‘N’ x ‘N’, onde as posições (x ;
y) e (y ; x) representam a distância entre os planetas x e y.

Obs.: Um dado código de planeta possui uma posição ‘p’ na lista de códigos de planetas dada, ou
seja, se foi dada uma lista com 3 códigos, então o primeiro planeta tem posição ‘p’ = 0, o segundo
planeta tem posição ‘p’ = 1, e assim sucessivamente. Sendo o planeta com posição ‘x’ e o planeta
com posição ‘y’ na lista de códigos, para saber a distância entre ‘x’ e ‘y’ basta acessar as posições (x ;
y) ou (y ; x) da matriz de distâncias, ou seja, dado o planeta ‘x’ = 1 e o planeta ‘y’ = 2, acesse matriz
na posição (1 ; 2) ou (2 ; 1). Mestre Yoda sempre começa do planeta na posição 0 (zero). Os planetas
possuem códigos diferentes.

### Saída

​	Imprima a distância total percorrida por Yoda.

| Entrada                                                      | Saída |
| ------------------------------------------------------------ | ----- |
| 3<br/>ADFXDE DFCDFG LPXDFH<br/>2<br/>LPXDFH DFCDFG<br/>0 2 3<br/>2 0 5<br/>3 5 0 | 8     |
| 4<br/>ABCDEF BCDEFG CDEFGH DEFGHI<br/>3<br/>BCDEFG CDEFGH DEFGHI<br/>0 1 2 3<br/>1 0 1 2<br/>2 1 0 1<br/>3 2 1 0 | 3     |

