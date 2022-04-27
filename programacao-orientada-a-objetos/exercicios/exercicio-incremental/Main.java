import java.util.Date;

public class Main {
  public static void main(String[] args){

    Date data = new Date(27/07/2001);

    Doador doador = new Doador("Caio","Pessoa Física","07248125555",data,"Doutor Filinto Borja","Ap 305 A","Brotas",85);

    Aplicacao ap = new Aplicacao(doador);
    ap.menu();

  }
}