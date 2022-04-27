package Classes;

public class Amador extends Jogador{

  public int bonus;

  public Amador(String nome, int cash){
    super(nome,cash);
    bonus = 0;
  }

  @Override
  public void ganha(){
    super.score+=50;
    super.score +=(50 * 0.20); //Ganha mais 20%
    bonus +=100;
  }

  @Override
  public void perde(){
    if(super.score <= 50 - (50 * 0.20)){
      super.score = 0;
    }else{
      super.score-=50;
      super.score +=(50 * 0.20); //Perde menos 20%
      bonus +=20;
    }
  }


}