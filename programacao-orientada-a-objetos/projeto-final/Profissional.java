package Classes;

import java.util.Scanner;
import java.util.ArrayList;

public class Profissional extends Jogador{

  private ArrayList<String> colecaoSkins = new ArrayList<String>();
  private String skin;
  
 
  public Profissional(String nome, int cash){
    super(nome,cash);
    skin = "Samurai";
    this.colecaoSkins.add(skin);
  }
  
  public String getSkin() {
    return skin;
  }

  public void setSkin(String skin) {
    this.skin = skin;
    this.colecaoSkins.add(skin);
  }

  public ArrayList<String> getColecao(){
    return colecaoSkins;
  }

  @Override
  public void ganha(){
    Scanner ler = new Scanner(System.in);
    super.score+=50;
    super.score +=(50 * 0.50); //Ganha mais 50%
    System.out.println("Escolha sua nova skin: ");
    this.skin = ler.nextLine();
    this.colecaoSkins.add(skin);
    
  }

  @Override
  public void perde(){
    if(super.score <= 50 - (50 * 0.5)){
      super.score = 0;
    }else{
      super.score-=50;
      super.score +=(50 * 0.50); //Perde menos 50%
    }
  }

}
