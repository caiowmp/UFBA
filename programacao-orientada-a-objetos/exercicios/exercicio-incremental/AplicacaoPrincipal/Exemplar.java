package AplicacaoPrincipal;


class Exemplar{

  private Livro livro;
  private boolean emprestado;

  public Exemplar(Livro livro,boolean emprestado){
    this.livro = livro;
    this.emprestado = emprestado;
  }

  public void setLivro(Livro livro){
    this.livro = livro;
  }

  public Livro getLivro(){
    return livro;
  }

  public void setEmprestado(boolean emprestado){
    this.emprestado = emprestado;
  }

  public boolean getEmprestado(){
    return emprestado;
  }
}



/*/Criar a classe Exemplar com os seguintes atributos:
 livro: tipo Livro
 emprestado: (true: se o livro foi emprestado; ou false: se o livro não foi emprestado): tipo Boolean
Obs: Cada exemplar pode agregar um livro. 
/*/