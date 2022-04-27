package Classes;

public abstract class Jogador{

  private String nome;
  protected double score;
  private static int idBase = 16841321;
  private int idFinal;
  private int cash;

  //Construtor de um jogador que usa cash 
  //Sobrecarga
  public Jogador(String nome, int cash){
    this.setNome(nome);
    score = 0;
    setIdFinal(idBase + 1);
    idBase++;
    this.setCash(cash);
  }

  //Construtor de um jogador que não usa cash 
  //Sobrecarga
  public Jogador(String nome){
    this.setNome(nome);
    score = 0;
    setIdFinal(idBase + 1);
    idBase++;
    setCash(0);  
  }

  public int getIdFinal() {
    return idFinal;
  }

  public void setIdFinal(int idFinal) {
    this.idFinal = idFinal;
  }

  public int getCash() {
    return cash;
  }

  public void setCash(int cash) {
    this.cash = cash;
  }

  public String getNome() {
    return nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public abstract void ganha();

  public abstract void perde();
  

  public void addCash(int cash){
    this.setCash(cash);
  }

  public double getScore(){
    return score;
  }
}