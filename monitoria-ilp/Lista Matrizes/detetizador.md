# 								Detetizador do Futuro

​																			Autor: Gabriel Lecomte

​	Jonathan é um estagiário da prestigiada Macrosoft, o que muitos não sabem é que ele está muito frustrado, pois acaba de descobrir que tudo que é feito lá nunca funciona. Como Jonathan não consegue mais trabalhar, ele decidiu criar um jogo para passar o tempo1. No jogo Detetizador do Futuro, o seu objetivo é matar todos os bugs que aparecem na tela (um bug morre quando levar um tiro), e Jonathan pediu para que você o ajudasse, escrevendo a parte do código que diz se o jogador ganhou ou perdeu.

### Entrada

​	A primeira linha é composta por dois inteiros ‘N’ e ‘M’ (1 <= N, M <= 10), correspondentes, respectivamente, ao número de linhas e de colunas da matriz que será passada como entrada. As próximas ‘N’ linhas terão cada uma ‘M’ inteiros ‘P’ (0 <= P <= 1), representando um bug ou não naquela posição. Uma posição com 0 não existe bug, ao passo que em uma posição com 1 existe bug. A próxima linha será composta por um inteiro ‘A’ (1 <= A <= 1000), correspondente ao número de tentativas de acertar um bug. As ‘A’ linhas seguintes, cada uma com dois inteiros ‘L’ e ‘C’ (1 <= L, C <= 10) indicam a posição do bug a ser atingido (se houver).

### Saída

O programa deverá imprimir “HASTA LA VISTA BABY” se todos os bugs forem mortos e “ILL BE BACK” caso contrário.

| Entrada                                   | Saída               |
| ----------------------------------------- | ------------------- |
| 2 2<br/>1 0<br/>0 1<br/>2<br/>1 1<br/>2 2 | HASTA LA VISTA BABY |
| 2 2<br/>1 1<br/>1 0<br/>2<br/>1 1<br/>1 2 | ILL BE BACK         |

