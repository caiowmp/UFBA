beecrowd | 2159

# Número Aproximado de Primos

Por M.C. Pinto, UNILA ![BR](https://resources.beecrowd.com.br/gallery/images/flags/br.gif) Brazil

**Timelimit: 1**

Schoenfeld e Rosser publicaram em 1962 um artigo descrevendo um valor mínimo e máximo para a quantidade de números primos até **n**, para **n** ≥ 17. Esta quantidade é representada pela função **(n)** e a fórmula é mostrada abaixo.

![img](https://resources.beecrowd.com.br/gallery/images/contests/931.png)

Sua tarefa é, dado um natural **n**, calcular o mínimo e máximo do intervalo para o número aproximado de primos até **n**.

## Entrada

A entrada é um número natural **n** (17 ≤ **n** ≤ 109).

## Saída

A saída são dois valores **P** e **M** com 1 casa decimal cada, tal que **P** < **(n)** < **M**, de acordo com a fórmula dada acima. Os valores devem ser separados por um espaço em branco.

| Exemplos de Entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 17                  | 6.0 7.5           |
| 50                  | 12.8 16.0         |
| 100                 | 21.7 27.3         |