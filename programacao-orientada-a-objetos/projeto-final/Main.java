package Aplicação;

import Classes.*;
import java.util.ArrayList;
import java.util.Scanner;

class Main {
  public static void main(String[] args) {

    int op=0; 
    Scanner ler = new Scanner(System.in);

    Jogador jog1 = new Iniciante("Jubileu");
    Jogador jog2 = new Amador("Ferinha", 50);
    Jogador jog3 = new Profissional("Neymar", 200);
    Jogador jog4 = new Estrela("Ronivan", 700);
    Jogador jog5 = new Iniciante("Caio");
    
    ArrayList<Jogador> players = new ArrayList<>();

    players.add(jog1);
    players.add(jog2);
    players.add(jog3);
    players.add(jog4);
    players.add(jog5);

    Jogo jogo1 = new Jogo("ajnksa", players);

    
    do{
      System.out.println("--------------Escolha a opção desejada--------------");
      System.out.println("1 - Listar Jogadores");
      System.out.println("2 - Listar Iniciantes");
      System.out.println("3 - Listar Amadores");
      System.out.println("4 - Listar Profissionais");
      System.out.println("5 - Listar Estrelas");
      System.out.println("6 - Adicionar Jogadores");
      System.out.println("7 - Todos Ganharam");
      System.out.println("8 - Todos Perderam");
      System.out.println("9 - Adicionar Skin");
      System.out.println("10 - Trocar Skin");
      System.out.println("0 - Sair");
      System.out.println("Digite o número da opção desejada: ");
      op = ler.nextInt();

      switch(op){
        case 1:
          Teste.listarJogadores(jogo1);
          break;
        case 2:
          Teste.listarIniciantes(jogo1);
          break;
        case 3:
          Teste.listarAmadores(jogo1);
          break;
        case 4:
          Teste.listarProfissionais(jogo1);
          break;
        case 5:
          Teste.listarEstrelas(jogo1);
          break;
        case 6:
          Teste.addJogador(jogo1);
          break;
        case 7:
          Teste.ganha(jogo1);
          break;
        case 8:
          Teste.perde(jogo1);
          break;
        case 9:
          Teste.novaSkin(jogo1);
          break;
        case 10:
          Teste.trocarSkin(jogo1);
          break;
        case 0:
          break;
        default:
          System.out.println("Digite uma opção válida!");
          break;
      }

    }while(op!=0);
    
    
  }
}
