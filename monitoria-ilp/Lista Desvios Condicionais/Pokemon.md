# 																Pokémon GO – Appraise

​	Ash está caçando pokémon com os amigos. No fim da caçada, ele ficou um pouco triste por ter capturado apenas um Pikachu, mas se manteve esperançoso pois sabia que o Pikachu poderia ser muito forte. Então, resolveu pedir sua ajuda para calcular a força do pokémon dele somando a quantidade de ataque, defesa e poeira que o Pikachu possui. Ash também pediu para que você seja discreto ao falar a porcentagem de força, pois não queria que os amigos soubessem.

​	Você, como Treinador pokémon, sabe que o pokémon mais forte tem no máximo 110 de força, se passar disso há algo errado, portanto, cuidado. Então, você decidiu fazer um cálculo para definir em porcentagem o quão forte é o pokémon de Ash, e irá comunicar a porcentagem através de frases para que os amigos dele não descubram a força do pokémon. Considere a porcentagem com apenas a parte inteira do cálculo.

| Porcentagem da Força | Frase                                       |
| -------------------- | ------------------------------------------- |
| Entre 0% a 50%       | "Seu pokemon nao far progresso em batalhas" |
| Entre 51% a 66%      | “Seu pokemon esta acima da media”           |
| Entre 67% a 79%      | “Seu pokemon certamente me chamou atencao”  |
| Entre 80% a 100%     | “Seu pokemon e uma maravilha”               |



## Entrada 

​	A primeira linha contêm três inteiros A (0 < A <= 40), D (0 < D <= 40) e P (0 < P <= 40) que são os valores de ataque, defesa e poeira do Pokémon.

## Saída 

​	Você deverá exibir a frase referente a porcentagem que o pokémon tem de força. Caso o pokémon tenha um valor acima do máximo esperado, exiba a frase “Hum, parece que houve um erro”.

## Exemplos 

| Entrada  | Saída                                      |
| -------- | ------------------------------------------ |
| 40 20 10 | Seu pokemon esta acima da media            |
| 40 30 20 | Seu pokemon e uma maravilha                |
| 20 10 10 | Seu pokemon nao fara progresso em batalhas |
| 40 40 35 | Hum, parece que houve um erro              |