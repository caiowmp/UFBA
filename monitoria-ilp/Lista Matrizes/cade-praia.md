# 								Oxi véi, cadê a praia?

​																Autor: Hérus Conceição

​	Você está desenvolvendo um programa de navegação marítima e exploração de ilhas.
​	Você percebeu que o Dev responsável pelo mapa se esqueceu de um detalhe: as praias.
​	Você precisa resolver esse problema criando um programa que transforma em praia aquilo que deveria ser praia.

### Entrada

​	A entrada será dada por um mapa de dimensões 10x10. Cada uma das 10 linhas de entrada possuirá 10 caracteres separados por espaços, sendo cada caractere ou ‘*’ para representar a água ou ‘t’ para representar a terra.

### Saída

​	O programa deve imprimir o mapa corrigido, transformando em praia ‘p’, todo
pedaço de terra ‘t’ que estiver em contato direto com a água ‘*’, verticalmente
ou horizontalmente. O que estiver fora do mapa não deve ser considerado como
água.

| Entrada                                                      | Saída                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| * * * * * * * * * *<br/>* * t t t t * * * *<br/>* t t t t t t * * *<br/>* * * * t t t t t *<br/>* * * * * t t t t *<br/>* * * * * t t t * *<br/>* * * * t t t t * *<br/>t t t t t t t t t *<br/>t t t t t t t t * *<br/>t t t t t * * * * * | * * * * * * * * * *<br/>* * p p p p * * * *<br/>* p p p t t p * * *<br/>* * * * p t t p p *<br/>* * * * * p t t p *<br/>* * * * * p t p * *<br/>* * * * p t t p * *<br/>p p p p t t t t p *<br/>t t t t t p p p * *<br/>t t t t p * * * * * |
| t * * * * * * * * t<br/>* t t t t t t t t *<br/>* t t t t t t t t *<br/>* t t t t t t t t *<br/>* t t t t t t t t *<br/>* t t t t t t t t *<br/>* t t t t t t t t *<br/>* t t t t t t t t *<br/>* t t t t t t t t *<br/>t * * * * * * * * t | p * * * * * * * * p<br/>* p p p p p p p p *<br/>* p t t t t t t p *<br/>* p t t t t t t p *<br/>* p t t t t t t p *<br/>* p t t t t t t p *<br/>* p t t t t t t p *<br/>* p t t t t t t p *<br/>* p p p p p p p p *<br/>p * * * * * * * * p |

