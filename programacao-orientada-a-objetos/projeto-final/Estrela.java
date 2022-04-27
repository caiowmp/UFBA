package Classes;

public class Estrela extends Jogador{

  public static int forca = 1000;

  public Estrela(String nome, int cash){
    super(nome,cash);
  }

  @Override
  public void ganha(){
    super.score+=50;
    super.score +=(50 * 0.90);  //Ganha mais 90%
  }

  @Override
  public void perde(){
    if(super.score <= 50 - (50 * 0.90)){
      super.score = 0;
    }else{
      super.score-=50;
      super.score +=(50 * 0.90);  //Perde menos 90%
    }
  }

}