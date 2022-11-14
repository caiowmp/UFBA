# Resposta 

Se não conseguiu usar o Google Classroom, coloque sua resposta aqui.

MATA56 - E3 - Exercícios praticos sobre conceitos de LP
NOME: Caio Miranda Pereira

Qual dos seguintes nomes de identificador é mais legível? Justifique sua resposta.
   SumOfSales
               sum_of_sales
               SUMOFSALES
Algumas linguagens de programação (LP) não têm tipo (typeless). Quais são as vantagens e desvantagens de não ter tipos em uma LP?
Escreva um comando de atribuição simples com um operador aritmético em alguma LP que você usa. Para cada elemento da atribuição, liste as várias amarrações (bindings) necessárias para determinar a sua semântica quando a instrução for executada. Para cada amarração, indique o tempo de amarração usado pela LP.
A amarração de tipos dinâmica está intimamente relacionada às variáveis dinâmicas de pilha implícitas (implicit heap-dynamic variables).  Explique essa relação.
Descreva uma situação em que uma variável sensível ao histórico em um subprograma é útil.
Considere a estrutura de um programa JavaScript:
	
// The main program 
var x;							
	function sub1() { 
     var x;							
     function sub2() { … } 
}							
function sub3() {
...							
}
Considere a execução deste programa com as seguintes chamadas (calls): 
main calls sub1
	sub1 calls sub2
sub2 calls sub3 				
Com escopo estático, qual a declaração de x correta para uma referência a x em:
sub1 
sub2 
sub3
Repita o exercício do item a), mas com escopo dinâmico.

Considere que o programa JavaScript abaixo foi interpretado usando regras de escopo estático. Qual é o valor de x mostrado por document.write (função sub1)? E, com regras de escopo dinâmico, qual o valor de x mostrado por document.write (função sub1)?  
     var x;
     function sub1() {							
     	 document.write("x = " + x + "<br />");
     }								
     function sub2() { 
var x;								
  	x = 10;							
  	sub1(); 
      }							
     x = 5; 
     sub2(); 	
						
Considere que o programa JavaScript abaixo:
 								
var x, y, z; 
     function sub1() {
 	    var a, y, z; 
    function sub2() {
        var a, b, z;					
        ... 
    }								
    ... 
     }
								
     function sub3() { 
   var a, x, w; 
   ...								
     } 


Liste todas as variáveis, junto com as unidades de programa onde elas são declaradas, que são visíveis nos corpos de sub1, sub2 e sub3, supondo que escopo estático seja usado.

Considere o programa Python a seguir:
 x = 1;   y = 3;	 z = 5;
 	def sub1():						
		a = 7; 
y = 9; 
z = 11; 
...
 								
def sub2(): 
global x; 
a = 13; 
x = 15; 
w = 17; 
...
 								
	def sub3(): 
nonlocal a; 
a = 19;
b = 21;
z = 23; 
...								
... 
 							
Liste todas as variáveis, junto com as unidades de programa onde elas são declaradas, que são visíveis nos corpos de sub1, sub2 e sub3, supondo que escopo estático seja usado.

Considere o programa C a seguir:
void fun(void) {
    int a, b, c;    /* definition 1 */								
    ...
    while (...) {								
          int b, c, d;    /*definition 2 */	
          ...  (i) 
          while (...) {	
              int c, d, e;    /* definition 3 */
               ... (ii) 
          }			
         ... (iii)								
    }			
    ... (iv) 								
} 
Para cada um dos quatro pontos marcados em fun (i, ii, iii, iv), liste cada variável visível e o número da declaração que a define (1, 2 ou 3).
Considere o programa C a seguir:
void fun1(void); /* prototype */ 
void fun2(void); /* prototype */ 
void fun3(void); /* prototype */ 
void main() { 
    int a, b, c;
    ... 
}
void fun1(void) {
     int b, c, d; 
    …
}
void fun2(void) {
    int c, d, e;
    ... 
}
void fun3(void) { 
    int d, e, f; 
    …
}

Considere as sequências de chamadas a seguir e uso de escopo dinâmico. Quais as variáveis visíveis durante a execução da última função chamada? Ao lado de cada variável visível, informe o nome da função na qual a mesma foi definida.			
a. main calls fun1; fun1 calls fun2; fun2 calls fun3. 
b. main calls fun1; fun1 calls fun3.
c. main calls fun2; fun2 calls fun3; fun3 calls fun1. 
d. main calls fun3; fun3 calls fun1.
e. main calls fun1; fun1 calls fun3; fun3 calls fun2.			
f. main calls fun3; fun3 calls fun2; fun2 calls fun1.

Considere o programa a seguir, escrito em uma sintaxe estilo JavaScript:
// main program 
var x, y, z;


function sub1() {
    var a, y, z;
    …
}
function sub2() {
    var a, b, z;
    ... 
}
function sub3() { 
    int a, x, w; 
    …
}

Considere as sequências de chamadas a seguir e uso de escopo dinâmico. Quais as variáveis visíveis durante a execução do último subprograma chamado? Ao lado de cada variável visível, informe o nome da unidade na qual a mesma foi declarada.			
a. main calls sub1; sub1 calls sub2; sub2 calls sub3. 
b. main calls sub1; sub1 calls sub3.
c. main calls sub2; sub2 calls sub3; sub3 calls sub1. 
d. main calls sub3; sub3 calls sub1.
e. main calls sub1; sub1 calls sub3; sub3 calls sub2.			
f. main calls sub3; sub3 calls sub2; sub2 calls sub1.


RESPOSTAS:
1) sum_of_sales, pois você percebe onde começa e onde termina cada palavra do identificador.
2) A grande vantagem é a praticidade ao escrever os códigos com a LP. Porém, uma desvantagem é que isso faz com que os programas sejam menos confiáveis, pois a capacidade de detecção de erros do compilador é diminuída. Outra desvantagem é que o custo de implementar a vinculação de atributos dinâmica, principalmente em tempo de execução, é enorme.
3) int x = y + 1
4) Essa relação se dá pois, ao declarar uma variável em uma LP com tipagem dinâmica, independe se a variável já foi usada anteriormente no programa ou como foi usada, a única coisa que interessa agora é o valor que foi atribuído a ela (variáveis dinâmicas do monte implícitas).
5) Uma situação onde uma variável estática é útil é quando você precisa utilizar a mesma variável em várias funções diferentes e acumular seu valor, fazendo com que seu valor seja atualizado e nunca seja perdido.
6) 
para todos os casos, declara a variável x no mian da seguinte forma: var x;
com o escopo dinâmico teremos que declarar a variável dentro das funções da seguinte forma: let x;
7) Em ambos os casos o resultado da função sub1() é ‘x = 5’
8) sub1: todas as variáveis declaradas na main e no escopo da própria função
    sub2: todas as variáveis declaradas na main, no escopo da própria função e no escopo da função sub1.
    sub3: todas as variáveis declaradas na main e no escopo da própria função
9) sub1: todas as variáveis declaradas na main e no escopo da própria função
    sub2: todas as variáveis declaradas na main, no escopo da própria função e no escopo da função sub1.
    sub3: todas as variáveis declaradas na main e no escopo da própria função
10) 
	i) 1,2
	ii) 1,2,3
	iii) 1,2
	iv) 1
