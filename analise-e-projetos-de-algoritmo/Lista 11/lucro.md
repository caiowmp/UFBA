beecrowd | 1310

# Lucro

Por TopCoder* ![img](https://resources.beecrowd.com.br/gallery/images/flags/us.gif) EUA

**Timelimit: 1**

George é dono de um circo e traz seu circo de cidade em cidade. Ele sabe o quanto de receita ele pode obter em qualquer dia de uma série de dias em uma cidade. Ele também sabe o custo constante diário para manter o seu circo. George quer trazer seu circo à cidade para a série de dias que resulta em maior lucro.

Por exemplo, se em uma determinada cidade o custo for de $ 20 por dia em um exemplo com 6 dias, sendo que as receitas previstas por dia são {$ 18, $ 35, $ 6, $ 80, $ 15, $ 21}, George pode obter o máximo de lucro trazendo o seu circo para esta cidade do dia 2 ao dia 4. Desta forma ele pode lucrar (35 + 80 + 6) - (3 * 20) = $ 61.

Nota: A série de dias que George traz seu circo para a cidade pode ser entre 0 e o número máximo de dias, inclusive. Obviamente, se George traz seu circo para a cidade por 0 dias, ele obtém $ 0 de lucro.

## Entrada

A entrada contém muitos casos de teste. A primeira linha de cada caso de teste contém um inteiro **N** (1 ≤ **N** ≤ 50) que representa o número de dias que George pode trazer o seu circo para a cidade. A segunda linha do caso de teste contém um número inteiro **custoPorDia** (0 ≤ **custoPorDia** < 1000) que representa o custo em manter o circo na cidade. Segue **N** linhas (uma por cada dia), contendo cada um um inteiro **receita** (0 ≤ **receita** < 1000) representa a receita que o circo obtem em cada dia. O final da entrada é indicado por EOF (fim de arquivo).

## Saída

Para cada caso de teste imprima o máximo de dinheiro que George pode ganhar trazendo o seu circo para a cidade de acordo com o exemplo abaixo.

| Exemplo de Entrada                                           | Exemplo de Saída |
| ------------------------------------------------------------ | ---------------- |
| 6<br/>20<br/>18<br/>35<br/>6<br/>80<br/>15<br/>21<br/>4<br/>40<br/>30<br/>20<br/>10<br/>38 | 61 <br />0       |