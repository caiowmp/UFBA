# Resposta 

Se não conseguiu usar o Google Classroom, coloque sua resposta aqui.

E2 - Questões para Revisão (individual) - 2022.2
NOME: Caio Miranda Pereira                       
O que é um sinônimo (alias) em uma LP? Dê exemplos.
O que é  l-value de uma variável? O que é  r-value? 
O que é "amarração" (binding)? O que é "tempo de amarração" (binding time)?
Após o projeto e a implementação de uma LP, quais os 4 tipos de binding time que podem acontecer em um programa escrito na LP?
Defina: amarração estática e amarração dinâmica.
Quais as vantagens e desvantagens de amarração dinâmica de tipos?                                        
Quais as vantagens e desvantagens de variáveis (a) estáticas, (b) dinâmicas de pilha, (c) dinâmicas explícitas (de heap) e (d) dinâmicas implícitas (de heap)?             
Defina: tempo de vida (lifetime), escopo, escopo estático e escopo dinâmico.
Qual o problema geral relacionado a escopo estático?
O que é “ambiente de referência” (referencing environment) de um comando?   
What is a static ancestor of a subprogram? What is a dynamic ancestor of a subprogram? 
O que é um "bloco" em uma LP?   
(Consulta: Livro de Robert Sebesta ou similar)

Respostas:

Apelido. Podemos dar apelidos (nomes diferentes) para uma variável já existente.
L-value: valor localizador, valor à esquerda que indica que podem ficar à esquerda do =. R-value: valor de uma expressão.
binding: associação de um identificador à uma entidade. binding time: tempo onde ocorre a amarração.
Tempo de execução, tempo de compilação, tempo de ligação e tempo de carga do programa.
Amarração estática: ocorre antes da execução do programa e permanece inalterada ao longo de toda a execução. Amarração dinâmica: a amarração ocorre ou é alterada durante a execução do programa.
 Vantagens: flexibilidade e generalidade. Desvantagens: Redução da capacidade de detecção de erro pelo compilador; Custo de implementação da vinculação dinâmica.
a) Vantagens:  poder utilizar a variável em vários lugares diferentes. Desvantagens: confusão ao criar muitas variáveis.
b) 
Tempo de vida: tempo em que uma variável está vinculada à uma posição específica da memória.
Escopo: partes do programa em que a variável é visível.
Escopo estático: quando o escopo de uma variável é definida antes da execução, ou seja, estaticamente.
Escopo dinâmico: quando o escopo de uma variável só é possível ser determinado em tempo de execução.
Problema relacionado à evolução de programas. Sistemas de software são altamente dinâmicos e estruturas que possuam escopo estático dificultam as mudanças e reestruturações necessárias para a evolução de um sistema.
 Coleção de todas as variáveis visíveis na sentença.
 Ancestral estático: Um escopo estático que aninha outro escopo
 Ancestral dinâmico: Um escopo dinâmico que aninha outro escopo 
 Os blocos são a unidade fundamental e podem representar comandos, condições, objetos e muitas outras variáveis que fazem parte da construção de um programa.
