# 									Temos que pegar!

​																		Autor: Elivelton Rangel

​	Ash Ketchum é um jovem treinador que está
iniciando sua jornada na região de Kanto, e sonha em
se tornar um verdadeiro mestre pokemon, descobrindo
o máximo de novos monstrinhos para registrar na sua
pokedex.
​	Ash precisa melhorar o sistema de sua pokedex,
incluindo opções de classificar os pokemons vistos por
nível ou nome, facilitando a busca por mais
informações, quando necessário.
​	Cada pokemon possui um nome e um nível de
força único inicial que determina o seu poder de batalha contra outros rivais.
​	Ajude Ash construindo um programa que classifique os pokemon por nível de
força ou pelo nome, podendo ambas as classificações serem exibidas em
ordem crescente ou decrescente. Ash só pode registrar um único pokemon de
determinado tipo, não havendo, portanto, repetições de tipo e de poder.

### Entrada

​	A primeira linha consiste de três informações, sendo a primeira um inteiro
‘Q’ (1 <= Q <= 151), representando a quantidade de pokemon que o
programa irá classificar. A segunda informação é um caractere que define a
forma de classificação dos pokemon, sendo ‘N’ para nome e ‘L’ para nível. E a
terceira informação é um caractere que indica a ordem de classificação, sendo
‘C’ para crescente e ‘D’ para decrescente. Cada uma das próximas ‘Q’ linhas
informam o nome de um pokemon com seu respectivo nível de força.

### Saída

​	Devem ser impressos os pokemon de forma ordenada, conforme a
configuração de entrada. Imprima o nome antes do nível, sempre.

| Entrada                                                      | Saída                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 5 N D<br/>Pikachu 9<br/>Bulbasaur 13<br/>Charmander 5<br/>Squirtle 3<br/>Caterpie 8 | Squirtle 3<br/>Pikachu 9<br/>Charmander 5<br/>Caterpie 8<br/>Bulbasaur 13 |
| 5 L C<br/>Pikachu 9<br/>Bulbasaur 13<br/>Charmander 5<br/>Squirtle 3<br/>Caterpie 8 | Squirtle 3<br/>Charmander 5<br/>Caterpie 8<br/>Pikachu 9<br/>Bulbasaur 13 |

