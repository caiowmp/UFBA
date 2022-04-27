# Polícia e Ladrão

Por Carlos Andrade ![BR](https://resources.beecrowd.com.br/gallery/images/flags/br.gif) Brazil

**Timelimit: 2**

Mario adora convidar seus amigos para brincar em sua casa. Então decidiu convidar seus amigos para brincarem de Polícia e Ladrão. O jogo consiste em dois grupos, um grupo é a polícia e o outro é o grupo dos ladrões. Os ladrões devem se esconder e a polícia deve capturá-los. Caso a polícia consiga capturá-los e prendê-los os ladrões perdem o jogo e caso a polícia não consiga capturá-los os ladrões vencem o jogo.

Mario decidiu que seria do grupo da polícia e que teria que procurar seus amigos do grupo dos ladrões e capturá-los, porém algum de seus amigos sentiram-se em desvantagens por não possuírem lugares estratégicos para se esconder no seu quintal.

Portanto decidiram planejar uma forma em que poderiam deixar os policiais sem saída e terem chances de ganhar o jogo. Para isso montaram um labirinto usando caixas de papelão e marcaram como “0” todos os lugares no quintal aonde os policiais poderiam atravessar e como “1” aonde os policiais não poderiam atravessar.

Os ladrões irão se esconder sempre no último espaço do labirinto, Se os policiais ficarem encurralados no labirinto os ladrões vencem e poderão comemorar a fuga, mas se os policiais alcançarem o ultimo espaço do labirinto os policiais serão os vencedores. Os policiais poderão andar somente nos blocos marcados como 0. Sua tarefa é determinar a partir do labirinto quem vai ganhar o jogo.

![img](https://www.urionlinejudge.com.br/gallery/images/contests/policia.jpg)

## Entrada

A primeira entrada consiste de um inteiro **T**(1 ≤ **T** ≤ 400) indicando o número de casos de testes.

As próximas **T** entradas consistem de uma matriz **5**x**5**, composta de valores inteiros, sendo 0 ou 1

## Saída

Seu programa deverá imprimir "COPS" caso o grupo dos policiais ganhem, e "ROBBERS" caso o grupo dos ladrões ganhem.

| Exemplo de Entrada                                           | Exemplo de Saída   |
| ------------------------------------------------------------ | ------------------ |
| 2<br /><br />0 0 0 0 1<br/>1 1 0 0 1<br/>0 1 0 0 0<br/>0 0 0 1 1<br/>1 1 0 0 0<br /><br />0 0 0 0 1<br/>1 1 0 0 1<br/>0 1 0 0 0<br/>0 0 1 1 1<br/>1 1 0 0 0 | COPS <br />ROBBERS |