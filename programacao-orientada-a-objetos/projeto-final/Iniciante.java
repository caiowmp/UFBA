package Classes;

public class Iniciante extends Jogador{

  public Iniciante(String nome){
    super(nome);
  }

  @Override
  public void ganha(){
    super.score+=50;
  }

  @Override
  public void perde(){
    if(super.score < 50){
      super.score = 0;
    }else{
      super.score-=50;
    }
  }

}