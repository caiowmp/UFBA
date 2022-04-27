package Aplicação;

import Classes.*;
import java.util.ArrayList;
import java.util.Scanner;


public class Jogo implements JogoGenerico{
  private String nomeJogo; 
  private ArrayList<Jogador> players;
  
    
  public Jogo(String nomeJogo, ArrayList<Jogador> jogadores){
    this.nomeJogo = nomeJogo;
    this.players = jogadores; //Agregação forte
  }

  public ArrayList<Jogador> getPlayers(){
    return players;
  }

  public void listarJogadores(){

    System.out.println("--------------Jogadores--------------");

    for(Jogador item : players){
        System.out.println("Nome: " + item.getNome());
        System.out.println("Id: " + item.getIdFinal());
        System.out.println("Cash: " + item.getCash());
        
        if(item instanceof Iniciante){
            System.out.println("Classificação: Iniciante");
        }else if(item instanceof Amador){
            System.out.println("Classificação: Amador");
        }else if(item instanceof Profissional){
            System.out.println("Classificação: Profissional");
        }else if(item instanceof Estrela){
            System.out.println("Classificação: Estrela");
        }

        System.out.println("--------------");
    }
  }

  public void listarIniciantes(){

      System.out.println("--------------Jogadores Iniciantes--------------");

      for(Jogador item : players){
          if(item instanceof Iniciante){
              System.out.println("Nome: " + item.getNome());
              System.out.println("Id: " + item.getIdFinal());
              System.out.println("Cash: " + item.getCash());
              System.out.println("--------------");
          }
      }
  }

  public void listarAmadores(){

      System.out.println("--------------Jogadores Amadores--------------");

      for(Jogador item : players){
          if(item instanceof Amador){
              System.out.println("Nome: " + item.getNome());
              System.out.println("Id: " + item.getIdFinal());
              System.out.println("Cash: " + item.getCash());
              System.out.println("--------------");
          }
      }
  }

  public void listarProfissionais(){

      System.out.println("--------------Jogadores Profissionais--------------");

      for(Jogador item : players){
          if(item instanceof Profissional){
              System.out.println("Nome: " + item.getNome());
              System.out.println("Id: " + item.getIdFinal());
              System.out.println("Cash: " + item.getCash());
              System.out.println("--------------");
          }
      }
  }

  public void listarEstrelas(){

      System.out.println("--------------Jogadores Estrelas--------------");

      for(Jogador item : players){
          if(item instanceof Estrela){
              System.out.println("Nome: " + item.getNome());
              System.out.println("Id: " + item.getIdFinal());
              System.out.println("Cash: " + item.getCash());
              System.out.println("--------------");
          }
      } 
  }

  public void ganha(){

      System.out.println("--------------Pontuação dos jogadores: --------------");

      for(Jogador item : players){
          System.out.println(item.getNome());
          System.out.println("Pontuação: " + item.getScore());
          System.out.println("--------------");
      } 

      System.out.println("---------Pontuação dos jogadroes após ganhar:---------");

      for(Jogador item : players){
          item.ganha();
          System.out.println(item.getNome());
          System.out.println("Pontuação: " + item.getScore());
          System.out.println("--------------");
      } 
  }

  public void perde(){

      System.out.println("--------------Pontuação dos jogadores: --------------");

      for(Jogador item : players){
          System.out.println(item.getNome());
          System.out.println("Pontuação: " + item.getScore());
          System.out.println("--------------");
      } 

      System.out.println("---------Pontuação dos jogadroes após perder---------");

      for(Jogador item : players){
          item.perde();
          System.out.println(item.getNome());
          System.out.println("Pontuação: " + item.getScore());
          System.out.println("--------------");
      } 
  }

  public void novaSkin(Profissional j){
      Scanner ler = new Scanner(System.in);
      System.out.println("Skin do jogador: " + j.getSkin());
      
      System.out.println("Escolha sua nova skin: ");
      j.setSkin(ler.nextLine());

      System.out.println("Nova Skin adicionada: " + j.getSkin());
      
  }

  public void addJogador(){
    String nome;
    int cash; 
    Scanner ler = new Scanner(System.in);
    Jogador jogador;
    
    System.out.println("Digite o nome do jogador: ");
    nome = ler.nextLine();
    System.out.println("Digite a quantidade de cash do jogador: ");
    cash = ler.nextInt();
    if(cash == 0){
        jogador = new Iniciante(nome);
        players.add(jogador);
    }else if(cash > 0 && cash < 101){
        jogador = new Amador(nome,cash);
        players.add(jogador);
    }else if (cash > 100 && cash < 501){
        jogador = new Profissional(nome,cash);
        players.add(jogador);
    }else if (cash > 500){
        jogador = new Estrela(nome,cash);
        players.add(jogador);
    }

   
  }

  public void trocarSkin(Profissional jogador){
    Scanner ler = new Scanner(System.in);
    int i = 1;
    System.out.println("Skin atual do jogador: " + jogador.getSkin());

    System.out.println("Escolha uma das skins disponíveis: ");

    for(String item : jogador.getColecao()){
        System.out.println(i + " - " + item);
        i++;
    }

    for( i = 0; i<1; i++){
        try{
            jogador.setSkin(jogador.getColecao().get(ler.nextInt() - 1));
        }catch(IndexOutOfBoundsException e){
            System.out.println("ERRO: O valor escolhido não corresponde a uma posição da sua coleção de skins\nTente novamente");
            i--;
        }
    }
    
    System.out.println("Skin do jogador após a troca: " + jogador.getSkin());

    
  }
    
    public String getNomeJogo() {
        return nomeJogo;
    }

    public void setNomeJogo(String nome) {
        nomeJogo = nome;
        
    }
   
}
