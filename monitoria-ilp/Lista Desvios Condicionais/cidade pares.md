# 									A Cidade dos Pares 

​																			Autor: João Pedro Rodrigues 

​	Capturar Pokémon é uma tarefa bastante simples. Você pode enfraquecer um Pokémon com uma batalha, ou conquistar seu afeto de alguma maneira e, em seguida, lançar um tipo de esfera própria para capturar pokémon conhecida como pokébola. Alguns pokémon são muito mais difíceis de capturar do que outros e, por isso, existem pokébolas mais resistentes que a pokébola comum, como por exemplo a famosa Master Ball. 

​	O que muita gente não sabe é que existe um lugar onde é possível capturar qualquer pokémon utilizando as pokébolas comuns, bastando apenas que esse pokémon esteja com um nível de resistência de valor par. Esse lugar é conhecido como Cidade dos Pares. 

​	Ash é um treinador conhecido por ser bastante carinhoso com seus pokémons. Ele pretende ir até a cidade dos pares e capturar o máximo de pokémon possível sem travar nenhuma batalha. Assim, desenvolva um programa que, dada a resistência de um pokémon, informe se Ash poderia capturá-lo sem batalhar, e se seria possível capturá-lo com uma pokébola simples se ele não estivesse na Cidade dos Pares. Saiba que a pokébola simples só é capaz de domar pokémon de até 10 mil pontos de resistência em outros lugares. 

## Entrada 

​	Será dado um valor N (0 <= N <= 100000) que representa o valor de resistência de um pokémon. 

## Saída 

​	A saída é composta de 2 linhas. A primeira linha conterá o valor ‘S’, caso Ash possa capturar o pokémon e ‘N’, caso contrário. A segunda linha conterá o valor ‘S’, se for possível capturar o pokémon usando uma pokébola simples fora da Cidade dos pares, e ‘N’, caso contrário. 

| Exemplo de entrada | Saída    |
| ------------------ | -------- |
| 17880              | S<br />N |
| 10000              | S<br />S |
| 10001              | N<br />N |