# Aula de Defesa contra as Artes das Trevas – There and Back Again

​	O novo professor de defesa contra as Artes das Trevas,
o elfo Dobbysley, ensinará a seus alunos da UFBA
(Universidade de Feitiçaria para Bruxos Anônimos) como se
defender do maligno Mausirius Black, que está a solta. Para a
primeira aula, o professor Dobbysley deu a seus alunos
diversos feitiços, que são formados por várias runas (pedras
mágicas), e a tarefa deles é descobrir quais desses feitiços
são proibidos, para que assim aprendam a diferenciá-los e
manipulá-los corretamente. Sua tarefa é ajudar os alunos
escrevendo um programa que descubra quais feitiços dados
por Dobbysley são proibidos, dadas uma lista de feitiços
gerais e uma lista de feitiços proibidos.

### Entrada

​	A entrada consiste de um inteiro ‘N’ (100 <= N <= 10000), indicando o número de feitiços gerais
dados pelo professor. Em seguida, serão dados ‘N’ feitiços, onde cada feitiço possui no máximo 5 runas
(Cada runa é indicada por uma letra do alfabeto de ‘A’ a ‘Z’). A seguir será dado um inteiro ‘M’ (100 <= M
<= 10000) , indicando o número de feitiços proibidos dados pelo professor. Em seguida, serão dados ‘M’
feitiços, onde cada feitiço possui no máximo 5 runas. Os feitiços nas duas listas já estão ordenados
crescentemente, ou seja, em ordem alfabética. Por fim, será dado um inteiro ‘C’ (10000 <= C <=
100000), representando o número de consultas a serem feitas. A seguir, serão dados ‘C’ feitiços e você
deverá dizer se são proibidos ou não. As consultas não possuem feitiços que não estejam
catalogados nas listas dadas, ou seja, ou o feitiço é geral ou ele é proibido, portanto fica a dica.

### Saída

​	Seu programa deve imprimir para cada feitiço a sua classificação, se é feitiço “Geral” ou “Proibido”,
de acordo com as listas dadas por Dobbysley. Imprima um por linha, de acordo com o exemplo abaixo.

| Entrada                                                      | Saída                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| 4<br/>ABCDE BCDEF CDEFG DEFGH<br/>3<br/>ABCDF BCDEG CDEFH<br/>5<br/>ABCDE ABCDF BCDEF BCDEG CDEFH | Geral<br/>Proibido<br/>Geral<br/>Proibido<br/>Proibido |

