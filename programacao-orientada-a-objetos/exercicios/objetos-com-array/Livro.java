class Livro{

  private String título;
  private String autor;
  private int edicao;
  private int qtd;

  public Livro(String título, String autor, int edicao, int qtd){

    this.título = título;
    this.autor = autor;
    this.edicao = edicao;
    this.qtd = qtd;
  }

  public String getTítulo(){
    return título;
  }

  public String getAutor(){
    return autor;
  }

  public int getEdicao(){
    return edicao;
  }

  public int getQtd(){
    return qtd;
  }
}