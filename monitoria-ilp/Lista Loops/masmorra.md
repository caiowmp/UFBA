# 											Masmorra 

​	Estamos prestes a entrar em uma masmorra com diversos perigos e aventuras. O princípio da aventura é vencer a masmorra e sair de lá com todos os seus tesouros ou morrer tentando. A aventura começa com o seu personagem no Lv 1 (Nível 1), termina imediatamente quando ele atinge o Lv 5 ou caso seja derrotado por um monstro. 

### Entrada 

​	A entrada se inicia com um inteiro N (1 < N <= 20), representando o número de portas que serão abertas na masmorra. A partir da linha seguinte, a entrada consiste em uma sequência de caracteres e inteiros, um por linha, que representam o que acontecerá após abrir cada uma das N portas da masmorra. Podendo cada caracter ser:

- ‘t’ - Encontramos em dada porta um tesouro. Logo após, na mesma linha, temos um inteiro q (1 <= q <= 2), assim, o nível do personagem aumenta em q (+1 Lv ou +2 Lv). 

- ‘m’ - Encontramos um monstro ao abrir determinada porta. Logo após, na mesma linha, temos um inteiro f (1 <= f <= 5), representando a força do monstro. Nesse caso, vencemos o combate e ganhamos mais 1 nível (+1 Lv) se o nosso nível for maior ou igual a f. Caso contrário, somos derrotados. 

- ‘b’ - Uma maldição que cai de forma imediata. Logo após, na mesma linha, temos um inteiro c (1 <= c <= 2), ou seja, o nível do personagem diminui em c (-1 Lv ou -2 Lv). 

- Cuidado pois o nível do personagem no mínimo será zero, porém o jogo não termina por causa dessa ocorrência. 

  ### Saída 

  ​	A saída consiste em um conjunto de strings, de acordo com os casos abaixo: 

- Sempre que acontecer um combate imprima “Combate iniciado”. Em seguida, na próxima linha, imprima “VITORIA”, se o combate for bem sucedido, caso contrário, imprima “Derrota! Fim da aventura”, terminando imediatamente o programa.

- Se o personagem atingir o Lv 5 imprima “Aventura concluida", terminando imediatamente o programa. 

- Caso nenhuma das situações acima ocorra, não imprima nada

  | Entrada                                   | Saída                                                        |
  | ----------------------------------------- | ------------------------------------------------------------ |
  | 4 <br />t 1 <br />t 1 <br />b 1 <br />m 3 | Combate iniciado <br />Derrota! Fim da aventura              |
  | 4 <br />t 1<br />t 1 <br />m 3 <br />m 1  | Combate iniciado <br />VITORIA <br />Combate iniciado <br />VITORIA <br />Aventura concluida |

  