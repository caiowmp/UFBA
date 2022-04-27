import java.util.Scanner;

class Main{

  public static void main(String[] args) {

    int qtdMaxLivros;

    Scanner ler = new Scanner(System.in);
    System.out.print("\nInforme a quantidade de livros: ");
    
    qtdMaxLivros = ler.nextInt();
    ler.close();

    Livraria saraiva = new Livraria("Saraiva","77851696", qtdMaxLivros);

    Livro l1 = new Livro("A Bela e a Fera","Fulano",1,5);

    saraiva.addLivro(l1);
    saraiva.imprimirLivrosAutor("Fulano");


    System.out.println("O livro " + l1.getTítulo() + " tem " + saraiva.getQtdExemplares("A Bela e a Fera") + " exemplares");
    

    saraiva.addLivro("Harry Potter","Fulana",3,7);
    saraiva.imprimirRelatório();



  }
}


