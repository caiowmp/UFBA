# 							Cuidado com o Sans 

​															Por M. Romano Saback Santos 

​	Em Undertale, Sans é um monstro que parece fraco, pois seus ataques dão apenas 1 de dano base. Mas ele tem um truque – toda vez que ele ataca, seus ataques podem dar, acumulado ao dano base, um dano especial, este sendo variável, mas que é aplicado múltiplas vezes em um só golpe. Entretanto, o dano especial é incapaz de matar o jogador, sempre deixando-o com pelo menos 1 HP. 

### Entrada

​	A entrada consiste, na primeira linha, de 2 inteiros, “H” e “V” (2 <= H <= 92, 1 <= V <= 50), que são o HP do jogador antes de ser atingido pelo ataque do Sans, e a quantidade de vezes que o dano especial será aplicado. Nas próximas “V” linhas, serão dados “V” inteiros D (0 <= D <= 5), um por linha, onde cada um deles se refere à quantidade de dano de cada aplicação do dano especial. Entretanto, atente que como o dano especial não pode ser letal, será aplicado apenas o que for possível. 

### Saída 

​	Na saída, você deverá exibir qual foi o dano total do ataque do Sans, recebido pelo jogador. 

| Entrada                                 | Saída |
| --------------------------------------- | ----- |
| 92 1<br />0                             | 1     |
| 92 5<br />1<br />2<br />4<br />5<br />5 | 18    |
| 6 4<br />1<br />2<br />3<br />4         | 5     |

