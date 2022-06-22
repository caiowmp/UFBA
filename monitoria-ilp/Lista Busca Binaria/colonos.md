# 										Colonos marcianos 2.0

​	Começou a era da colonização de novos mundos e o primeiro planeta
dessa aventura humana será Marte. Milhões de terráqueos se inscreveram para
concorrer a passagens só de ida.
​	Os responsáveis pelo projeto desenvolveram testes técnicos, físicos,
psicológicos e emocionais para testar os candidatos. Assim, serão selecionados
os mais aptos, ou seja, aqueles com maiores notas. Os candidatos também
possuem identificadores únicos que serão seus IDs em Marte. Esses IDs foram
gerados de forma que o candidato mais novo possui o menor ID e o candidato
mais velho possui o maior ID. Desta forma, em caso de empate quanto as notas,
se escolhe o(s) candidato(s) com a(s) menor(es) idade(s), ou seja, menor(es)
identificador(es).
​	Os candidatos estão eufóricos para saber se serão os novos colonos. Sabendo de seu talento em
programação o Prof. Rubisley te contratou para gerenciar esta delicada operação de seleção dos ‘N’ colonos
marcianos.

### Entrada

​	Primeiramente teremos um inteiro ‘N’ (2 ≤ ‘N’ ≤104
), representando a quantidade de candidatos que serão
selecionados, seguido de um inteiro ‘Q’ (106 ≤ ‘Q’ ≤ 109
), representando a quantidade total de candidatos. Na
sequência teremos ‘Q’ linhas contendo em cada uma dois inteiros ‘NQi’ (0 ≤ ‘NQi’ ≤ 104
) e ‘IdQi’ (1 ≤ ‘IdQi’ ≤109
),
representando respectivamente, a nota e o ID do candidato Qi. Na próxima linha teremos um inteiro ‘C’ (1 ≤ ‘C’ ≤ ‘Q’),
representando o número de consultas que serão feitas pelos candidatos. Nas próximas ‘C’ linhas serão fornecidos
dois inteiros ‘NCi’ e ‘IdCi’, representando respectivamente, a nota e o ID do candidato ‘Ci’ que quer saber se foi
selecionado, ou seja, se está dentre os ‘N’ selecionados.

### Saída

​	Seu programa deverá imprimir ‘Sim’ ou ‘Nao’, um por linha, para cada uma das consultas realizadas.

| Entrada                                                      | Saída               |
| ------------------------------------------------------------ | ------------------- |
| 5 10<br/>90 97<br/>78 25<br/>150 37<br/>200 57<br/>378 29<br/>766 20<br/>89 56<br/>36 45<br/>150 27<br/>888 35<br/>3<br/>766 20<br/>90 97<br/>888 35 | Sim<br/>Nao<br/>Sim |
| 3 5<br/>278 18<br/>197 35<br/>99 41<br/>85 33<br/>99 28<br/>2<br/>99 41<br/>99 28 | Nao<br/>Sim         |

