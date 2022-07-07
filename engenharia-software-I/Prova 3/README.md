# Atividade Avaliativa 3 – 06.07.2022

1. Os padrões de projeto, segundo o GoF, estão categorizados em: padrões de criação, padrões estruturais, 
e padrões comportamentais. Defina cada categoria, listando pelo menos dois padrões pertencentes a 
cada categoria. (0,5)
2.  Escreva o código de uma classe chamada Sistema que segue o padrão **Singleton**. Basta escrever o código 
relacionado ao padrão. Utilize a linguagem OO de sua preferência. (1,0)
3. Desenhe o diagrama de classes que representa graficamente o padrão descrito na questão anterior. 
Forneça um exemplo prático para auxiliar a ilustração (1,0).
4. Considere a seguinte situação:
Você tem uma sorveteria que permite que os clientes adicionem coberturas ao sorvete a depender do 
gosto deles. Na sorveteria, você tem um sistema que informa na tela, a depender dos ingredientes 
adicionados, a descrição e o preço final do sorvete. O valor do sorvete é fixo: R$5,00. Por enquanto, você 
só oferece dois tipos de coberturas: calda e passas. A porção de calda custa R$ 1,00 e a de passas, R$ 
1,50. O cliente pode adicionar quantas porções quiser de cada cobertura. Por exemplo, se o cliente 
adicionar duas porções de calda e uma de passas, o sorvete irá custar R$8,50 (5,00 + 1,00 + 1,00 + 1,50), 
e a descrição mostrada poderá ser: “Sorvete, calda, calda, passas”, a depender da ordem que o sorvete 
foi montado no sistema. Desenhe o diagrama de classes e escreva o código (na linguagem OO de sua 
preferência) para essa situação usando o padrão de projeto **Decorator**. Escreva também o método 
principal (em Java seria a “main(String[] args)”) de uma classe SorveteMaker que instancia 
um sorvete com duas porções de passas e uma de calda, e imprime no console (em Java, seria 
“System.out.println”) a descrição e o preço final desse sorvete. (2,5)