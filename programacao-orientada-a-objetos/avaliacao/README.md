# Prova de Programação Orientada a Objetos

## Universidade Federal da Bahia/Instituto de Matemática e Estatística/Departamento de Ciência da Computação
MATA55 – Programação Orientada a Objeto

Professora Rita Suzana Pitangueira Maciel

Primeira avaliação – 29/09/2021
## OBSERVAÇÕES:
- Utilize apenas os conceitos ministrados até o momento.
- Será analisado o uso correto do paradigma e do estilo de programação JAVA.
- Deve ser utilizado o repl.it e disponibilizar o link de compartilhamento.
## Cenário 01
Uma delegacia necessita de um sistema que ajude a gerenciar seus boletins de ocorrência. Uma
delegacia é cadastrada com seu nome, CNPJ, endereço, nome do delegado titular, além de um status,
que pode ser ativa ou inativa, caso a delegacia esteja fechada por prazo indeterminado. Além disso,
uma lista de boletins de ocorrência é registrada na delegacia. Um boletim de ocorrência (fato da
abertura do BO) possui como dados relevantes: o número do boletim de ocorrência, tipo de ocorrência
(que pode ser desabamento, incêndio, desaparecimento e assalto), detalhamento da ocorrência, data
e localização da ocorrência, nome (de quem registrou a ocorrência) e cpf (do solicitante da ocorrência.
Boletins de ocorrências não podem ser registrados em duplicidade na lista de uma determinada
delegacia e só pertencem a uma única delegacia. Quando uma delegacia é extinta os BO são
arquivados (saem do sistema ativo de delegacias). Com base no cenário, implemente as questões a
seguir.
## Questões
### 1.Sabendo que uma delegacia pode ter vários boletins, mas um boletim pertence apenas a uma delegacia, implemente os construtores de boletim de ocorrência e delegacia obedecendo o seguinte (4,0):
#### a) Um boletim de ocorrência pode ser cadastrado de duas formas: 

(1) informando todos os seus dados descritos no cenário;

(2) informando apenas os dados obrigatórios que são: o número do boletim de ocorrência, tipo de ocorrência, data, localização da ocorrência.

#### b) Uma delegacia pode ser cadastrada de duas formas: 

(1) informando todos os dados descritos no cenário; 

(2) caso não seja informado o status, considerar o status como inativa. A lista de boletins de ocorrência registrados na delegacia deve estar vazia neste momento.
### 2. Crie os seguintes métodos (3,0):
#### a) Um método que permita que um boletim de ocorrência seja adicionado à lista BOs de uma delegacia. (Lembre-se de verificar se esse BO já está na lista, não será permitido duplicatas).

#### b) Métodos que permitam que um boletim de ocorrência seja removido da lista de BOs de uma delegacia. Há duas possibilidades de parâmetros para o(s) método(s): 

(1) recebe o número do boletim de ocorrência como parâmetro;

(2) recebe uma instância de um boletim de ocorrência. O retorno deve ser true caso o boletim de ocorrência tenha sido encontrado e removido, ou false, caso contrário. Considerar que não existem boletins de ocorrência duplicados.
### 3. Crie métodos que permitam imprimir as informações dos boletins de ocorrência da delegacia da seguinte forma (3,0):
#### a) imprimir os dados da delegacia e a quantidade de boletins (sem parâmetros de entrada).
#### b) imprima os dados da delegacias e dos seus boletins de ocorrência e receba um parâmetro:
i) Se o parâmetro for true, imprima apenas os dados das delegacias ativas.

ii) Se o parâmetro for false, imprima apenas os dados das delegacias inativas

