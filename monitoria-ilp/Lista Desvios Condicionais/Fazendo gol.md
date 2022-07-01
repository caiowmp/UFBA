# 																		Fazendo um gol

​																				Autor: Julio Cesar

​	O jogo favorito de Lucas é Bomba Patch. Atualmente, ele está desenvolvendo uma forma de saber qual é o melhor lado para driblar o zagueiro adversário e chutar para o gol. Por isso ele pediu sua ajuda para desenvolver um programa que vai receber as direções que o zagueiro e o goleiro tentarão defender, e as direções que o atacante irá tentar driblar o zagueiro e chutar para gol, e diga se o atacante terá sucesso ou não.

## Entrada 

​	A entrada é composta por apenas duas linhas contendo dois caracteres em cada. Na primeira linha temos "z" e "g", sendo "z" a direção que o zagueiro irá para tentar bloquear o drible do atacante e "g" a direção que o goleiro irá tentar defender o chute do atacante. A segunda linha contém dois caracteres "d" e "c", que são respectivamente, a direção que o atacante irá tentar driblar o zagueiro, e se passar pelo zagueiro, a direção que o atacante irá chutar para o gol. Saiba que os valores possíveis para “z”, ”g”, “d” e “c” são esquerda ou direita, representados pelos caracteres ‘e’ e ‘d’, respectivamente.

## Saída 

​	A saída depende das seguintes situações: 1) no caso do zagueiro e atacante irem na mesma direção, só haverá uma linha na saída e deve-se imprimir a frase "Bloqueado"; 2) no caso de zagueiro e atacante irem em direções opostas, a frase impressa na primeira linha será "Driblado"; 3) caso o atacante tenha passado pelo zagueiro e o atacante chute na mesma direção que o goleiro foi para tentar defender, a frase impressa na segunda linha será "...e o goleiro pega"; 4) caso o atacante chute para um lado e goleiro vá para o outro a frase na segunda linha será "Gol".

​	**Obs.:** Só há a segunda linha na saída se o atacante passar pelo zagueiro. Sempre interprete os dados na perspectiva dos próprios jogadores, ou seja, para qual lado cada um vai.

## Exemplos 

| Entrada      | Saída                              |
| ------------ | ---------------------------------- |
| e e<br />e d | Driblado <br />...e o goleiro pega |
| d d<br />d d | Driblado<br />Gol                  |
| e d<br />d d | Bloqueado                          |
