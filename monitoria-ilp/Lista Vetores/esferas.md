# 					Em Busca das Esferas do Dragão

 Bulma quer reunir as 7 esferas do dragão para realizar o seu desejo. Para isso ela utilizará o radar do dragão para localizar as esferas, mas o radar está mostrando esferas que não deveriam existir. Sua tarefa é criar um programa que dado a quantidade e o número de estrelas de cada esfera do dragão encontrada, imprima quais das 7 esferas foram encontradas, e se é possível invocar shenlong. 

## Entrada

 Na primeira linha será dado um inteiro ‘N’ (1 <= N <= 1000) que diz a quantidade de esferas que o radar está mostrando. A próxima linha terá ‘N’ inteiros ‘E’ (1 <= E <= 1000), que correspondem ao número de estrelas de cada uma das ‘N’ esferas. Não há esferas repetidas com número de estrelas entre 1 e 7, mas acima disso podem se repetir. 

## Saída

 A saída consiste em 2 linhas, sendo que na primeira linha você deverá imprimir, em ordem crescente, as esferas com 1 a 7 estrelas que foram encontradas. A segunda linha terá duas possíveis frases: se as 7 esferas foram encontradas, deve-se imprimir “Saia Shenlong e realize o meu desejo”, caso falte alguma das 7 esferas, deve imprimir “Nao encontramos todas”.

| Entrada                         | Saída                                                   |
| ------------------------------- | ------------------------------------------------------- |
| 10<br />1 2 3 4 5 6 7 8 9 10    | 1 2 3 4 5 6 7<br />Saia Shenlong e realize o meu desejo |
| 10<br />1 3 7 9 10 11 6 4 12 15 | 1 3 4 6 7<br />Nao encontramos todas                    |
| 8<br />13 15 18 13 1 15 4 7     | 1 4 7<br />Nao encontramos todas                        |

