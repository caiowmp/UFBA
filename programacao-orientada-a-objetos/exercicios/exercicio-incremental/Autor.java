class Autor{

  private String nome;
  private String sexo;

  public Autor(String nome, String sexo){
    this.nome = nome;
    this.sexo = sexo;
  }

  public void setNome(String nome){
    this.nome = nome;
  }

  public String getNome(){
    return nome;
  }

  public void setSexo(String sexo){
    this.sexo = sexo;
  }

  public String getSexo(){
    return sexo;
  }
}

/*/Criar a classe Autor com os seguintes atributos:
 nome (nome Autor): tipo String
 sexo: tipo String
Obs: Cada livro pode agregar um ou vários autores. Se apagar o Autor, os livros continuam existindo. 
/*/