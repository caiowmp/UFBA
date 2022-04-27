class Livraria{
  
  private String nome;
  private String cnpj;
  private Livro[] livros;
  private int qtdLivros;

  public Livraria(String nome, String cnpj, int qtdMaxLivros){
    this.nome = nome;
    this.cnpj = cnpj;
    this.livros = new Livro[qtdMaxLivros];
  }

  // letra a
  public int getQtdExemplares(String nome){
    for(int i = 0; i < livros.length; i++){
      if(livros[i].getTítulo() == nome){
        return livros[i].getQtd();
      }
    }
    return 0 ;
  }

  // letra b
  public boolean addLivro(Livro livro){
    if(this.qtdLivros < this.livros.length){
      this.livros[qtdLivros] = livro;
      this.qtdLivros++;
      return true;
    }else{
      return false;
    }
  }

  public boolean addLivro(String nome, String autor, int edicao, int quantidade){
    if(this.qtdLivros < this.livros.length){
      Livro livro = new Livro(nome, autor, edicao, quantidade);
      this.livros[qtdLivros] = livro;
      this.qtdLivros++;
      return true;
    } else {
      return false;
    }
  }

  // letra c
  public void imprimirLivrosAutor(String autor){

    for(int i = 0; i < qtdLivros; i++){
      if(livros[i].getAutor() == autor){
        System.out.println(livros[i].getTítulo());
        System.out.println("\n");
      }  
    }
  }

  // letra d
  public void imprimirRelatório(){
    System.out.println(" ============\n");
    System.out.println(" Livraria " + this.nome + "\n");
    System.out.println(" Cnpj " + this.cnpj + "\n");
    System.out.println("===========================\n");
    System.out.println(" Livro              Autor.          Editora.        Exemplares Disponíveis\n");
    System.out.println("===========================\n");
    
    for(int i = 0; i < livros.length; i++){
      System.out.println(livros[i].getTítulo() + ".             " + livros[i].getAutor() + ".             " + livros[i].getEdicao() + ".             " + livros[i].getQtd() + "\n");
    }
    
    System.out.println("Total de Livros = " + this.qtdLivros + "\n");
  }

}