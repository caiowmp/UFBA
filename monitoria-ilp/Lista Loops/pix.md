# 									Limite PIX 2 

​	Diana pediu novamente para que você a ajude a controlar seus gastos. Dessa vez ela pede que enquanto o usuário (Diana) executar um valor de gasto diferente de 0.00 (zero ponto zero zero), o programa calcule o total de seus gastos e o quanto ela ainda possuirá de limite sobrando. Lembre-se que o limite dela é de R$2000.00 e ela quer R$150.00 disponíveis para gastar com outras coisas. Caso um número menor que 0(zero) seja digitado o programa terminará e mostrará a frase “Numero invalido”. 

### Entrada 

​	A entrada consiste de uma sequência de números reais X (0.00 <= X <= 2000.00), um por linha. A entrada termina com a ocorrência do valor 0.00 ou um valor negativo. 

### Saída 

​	Ao terminar a entrada com 0(zero), a execução é interrompida e o resultado é mostrado, imprimindo a frase “Passou o limite”, caso o valor total dos gastos seja maior que o limite definido por Diana, ou a frase “Valor total de X e L de limite disponivel”, onde X é o valor do total das contas e L o limite restante, caso o valor total seja menor que o limite estabelecido. Também poderá ser impressa a frase “Numero invalido”, caso a entrada em algum momento seja negativa. Imprima os valores com duas casas decimais de precisão.

| Entrada                         | Saída                                                |
| ------------------------------- | ---------------------------------------------------- |
| 1000.00 <br />851.00 <br />0.00 | Passou o limite                                      |
| 1850.00 <br />0.00              | Valor total de 1850.00 e 0.00 de limite disponivel   |
| 100.00 <br />200.00 <br />0.00  | Valor total de 300.00 e 1550.00 de limite disponivel |
| 200.00 <br />-1.00              | Numero invalido                                      |

