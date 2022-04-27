# Trabalho Final da disciplina de Programação Orientada a Objetos

#### Feito em conjunto com Kennedy Rocha

Um certo jogo online possui alguns tipos de jogadores, sendo eles, iniciante, amador, profissional e estrela. Todos os jogadores possuem um identificador, um nome criado pelo próprio jogador, um score que depende das suas partidas. E, por não ser um jogo totalmente justo, jogadores possuem ainda a possibilidade de comprar “cash”, atributo do jogo que definirá qual tipo de jogador você será, o que possibilitará uma bonificação diferente para cada um. O cash só é permitido adicionar no momento do cadastro. Todas essas características são comuns para todos os jogadores que se cadastrem (nome, score, identificador e quantidade de cash).

Os jogadores participam de partidas, e a depender do resultado obtido podem ter um aumento ou diminuição em seu score. Jogadores de tipo superior ganham mais score e perdem menos score. 

Os jogadores classificados como iniciantes possuem de 0 de cash em sua conta e pontuam a cada partida +50 caso ganhem e -50 caso percam (quantidade padrão de pontos).

Os amadores possuem de 1 a 100 de cash em sua conta e pontuam a cada partida +(50 * 1.20) pontos caso ganhem e -(50 * 0.80) caso percam (ganham 20% mais pontos e perdem 20% menos). Além disso, eles possuem uma quantidade de bônus que é ganho a cada partida, que podem ser trocados por benefícios no jogo.

Os profissionais possuem de 101 a 500 de cash em sua conta e pontuam a cada partida +(50 * 1.50) pontos caso ganhem e -(50 * 0.50) caso percam (ganham 50% mais pontos e perdem 50% menos). E também ganham uma skin nova de sua escolha a cada vitória, preenchendo, assim, sua coleção de skins. 

E, por fim, os estrelas possuem +501 de cash em sua conta e pontuam a cada partida +(50 * 1.90) pontos caso ganhem e -(50 * 0.10) caso percam (ganham 90% mais pontos e perdem 90% menos). Esse tipo possui uma força especial, definida por um valor fixo, que ajuda nas partidas. 

O sistema que simula o jogo, permite aos usuários utilizar diversas funções relacionadas ao jogo. Sendo elas, cadastrar todos os tipos de jogadores, adicionar novos jogadores, simular vitórias e derrotas nas partidas, listar todos os jogadores cadastrados com seus respectivos atributos, ou listar apenas os jogadores de um determinado tipo. E, ainda, para o tipo profissional, que possui coleção de skins, é possível trocar as skins e adicionar novas. 


## Para resolver o problema, e desenvolver o sistema, alguns conceitos de Orientação a Objetos foram utilizados, sendo eles:
### Herança: 
Como existem vários tipos de jogador com atributos em comum, é necessário usar o conceito de herança para criar uma classe mãe. Simplificando assim o desenvolvimento, e podendo reaproveitar código. 
### Classe Abstrata/ Métodos abstratos:
Em nosso sistema, todos os jogadores são de algum tipo, logo não é possível instanciar a classe mãe, Jogador. Para isso, fizemos que essa classe fosse abstrata. E definimos alguns métodos abstratos nela, para que cada classe descendente definissem da forma que lhe é necessário. 
### Sobreposição:
Usamos para sobrescrever os métodos da classe mãe, nas classes filhas. 
### Sobrecarga:
Utilizamos para ter mais de um método com o mesmo nome, neste caso, foi usado para criar os métodos construtores que possuem o mesmo nome, mas recebem diferentes parâmetros. 
### Polimorfismo:
Os dois citados anteriormente fazem parte do conceito de polimorfismo. Uma vez que este refere-se a um objeto poder se comportar da mais de uma forma.
### Composição:
Como precisamos ter um jogo que possui vários jogadores, usamos também o conceito de composição, para que isso fosse possível.
### Campos estáticos:
Para termos um id para cada jogador criado, usamos um atributo estático, possibilitando que ele seja incrementando a cada instância e mantenha a relação entre os ids. Cada novo jogador possuirá um id maior. 
### Cast e Instanceof:
Apenas jogadores do tipo profissional possuem o método trocar de skin, para identificar quais jogadores são desse tipo, usamos o instanceof. E atrelamos ao cast, para garantir que o método poderia ser usado. 
### Interface:
Para definir como deve ser um jogo implementado no sistema, usamos uma Interface para o jogo. Esta, mostra para o exterior as funcionalidades disponíveis no jogo. 
### Métodos Estáticos:
Definindo um padrão de testes para o sistema, criamos uma classe de testes que possui métodos estáticos. Estes possibilitam que sejam chamados e executados sem a necessidade de instanciar a classe. Já que a classe é apenas para fazer os testes.
### Pacotes:
Foram usados para deixar o sistema mais organizado, fazendo uma separação entre as classes e os arquivos relacionados a aplicação. 
### Comentário/ @Override:
Foram usados para marcar o código, deixando mais claro o que cada parte está fazendo. E o @Override, usado para garantir que os métodos serão sobrescritos.
