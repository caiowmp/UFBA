import java.util.ArrayList;
import java.util.Iterator;

class Livro{

  private String titulo_livro;
  private ArrayList<Autor>autor;
  private Integer ano;
  private Integer edicao;
  private Editora editora;
  private String isbn;
  private String classifição_livro;

  public Livro(String titulo_livro,ArrayList<Autor>autor,Integer ano,Integer edicao,Editora editora,String isbn,String classifição_livro){

    this.titulo_livro = titulo_livro;
    this.autor = autor;
    this.ano = ano;
    this.edicao = edicao;
    this.editora = editora;
    this.isbn = isbn;
    this.classifição_livro = classifição_livro;
  }

  public void setTituloLivro(String título_livro){
    this.titulo_livro = titulo_livro;
  }

  public String getTituloLivro(){
    return titulo_livro;
  }

  public void setAutores(ArrayList<Autor>autor){
    this.autor = autor;
  }

  public ArrayList<Autor> getAutores(){
    return autor;
  }

  public void setAno(Integer ano){
    this.ano = ano;
  }

  public Integer getAno(){
    return ano;
  }

  public void setEdicao(Integer edicao){
    this.edicao = edicao;
  }

  public Integer getEdicao(){
    return edicao;
  }

  public void setEditora(Editora editora){
    this.editora = editora;
  }

  public Editora getEditora(){
    return editora;
  }

  public void setISBN(String isbn){
    this.isbn = isbn;
  }

  public String getISBN(){
    return isbn;
  }

  public void setClassificacaoLivro(String classifição_livro){
    this.classifição_livro = classifição_livro;
  }

  public String getClassificacaoLivro(){
    return classifição_livro;
  }
}