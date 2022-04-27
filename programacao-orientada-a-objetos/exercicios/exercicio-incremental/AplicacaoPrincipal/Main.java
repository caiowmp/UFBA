package AplicacaoPrincipal;
import Classes.*;
import java.util.Date;

public class Main {
  public static void main(String[] args){

    Date data = new Date(26/07/2001);

    Pessoa doador = new Doador("Caio","Pessoa Jurídica","07248125555",data,"Doutor Filinto Borja","Ap 305 A","Brotas",85);

    System.out.println(doador.VerificaPessoa());

    /*/Aplicacao ap = new Aplicacao(doador);
    ap.menu();/*/

  }
}