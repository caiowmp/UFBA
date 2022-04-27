package AplicacaoPrincipal;
import java.util.Scanner;
import java.util.ArrayList;


class Aplicacao{

  static Scanner ler = new Scanner(System.in);
  static int escolha;
  private Pessoa doador;

  public Aplicacao(Pessoa doador){
    this.doador = doador;
  }

  /*/public static void menu(){
    System.out.println("Escolha uma opção:\n");
    System.out.println("1 - Adicionar doação\n");
    System.out.println("2 - Remover doação\n");
    System.out.println("3 - Atualizar Doação\n");
    System.out.println("4 - Listar doações\n");
    System.out.println("5 - Encerrar\n");

    escolha = ler.nextInt();

    switch(escolha){
      case 1:
        AdicionarDoacao();
        break;
      case 2: //Como assim remover doação ? Método destrutor ?
        RemoverDoacao();
        break;
      case 3: //Como saber de qual doação se trata ?
        AtualizarDoacao();
        break;
      case 4: //Imprimir uma lista de doações ou criar uma lista de doações ?
        ListarDoacao();
        break;
      case 5:
        System.out.println("Programa encerrado");
        break;
      default:
        System.out.println("Escola inválida");
        menu();
    }
  }

  public static void AdicionarDoacao(){

    Doacao doacao = new Doacao();

    System.out.println("Digite as informações da doação");
    System.out.println("Digite o tipo da doação");
    System.out.println("Descreve a doação");
    System.out.println("Qual o estado da doação ?");
    System.out.println("Digite a quantidade da doação");
    System.out.println("Ela pode ser entregue ?");
    System.out.println("Código da doação:\n" + doacao.codigo_doacao); //O protocolo a que vocês se referem é o código da doação ?
  }

  public static void RemoverDoacao(){

  
  }
  
  public static void AtualizarDoacao(){

    System.out.println("Digite as informações da doação");
    System.out.println("Digite o tipo da doação");
    System.out.println("Descreve a doação");
    System.out.println("Qual o estado da doação ?");
    System.out.println("Digite a quantidade da doação");
    System.out.println("Ela pode ser entregue ?");

  }

  public static void ListarDoacao(){

    
    
  }/*/
}