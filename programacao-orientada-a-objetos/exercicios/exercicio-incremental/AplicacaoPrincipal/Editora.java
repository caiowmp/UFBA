package AplicacaoPrincipal;

class Editora{

  private String nome;

  public Editora(String nome){
    this.nome = nome;
  }

  public void setNome(String nome){
    this.nome = nome;
  }

  public String getNome(){
    return nome;
  }
}

/*/Criar a classe Editora com os seguintes atributos:
 nome (nome do editora): tipo String
Obs: Cada livro pode agregar uma Editora. Se apagar a Editora, os livros continuam existindo/*/