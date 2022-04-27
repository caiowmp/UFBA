import java.util.Scanner;

class Calculadora{ // Sempre que colo public class da erro na hora de compilar '-'

  private double valor1;
  private double valor2;

  public Calculadora(){}

  public void setValor1(double valor1){
    this.valor1 = valor1;
  }

  public double getValor1(){
    return valor1;
  }

  public void setValor2(double valor2){
    this.valor2 = valor2;
  }

  public double getValor2(){
    return valor2;
  }

  public void Soma(){
    System.out.print(valor1+valor2);
  }

  public void Subtração(){
    System.out.print(valor1-valor2);
  }

  public void Multiplicação(){
    System.out.print(valor1*valor2);
  }

  public void Divisão(){
    System.out.print(valor1/valor2);
  }

}

public class Main {
  public static void main(String[] args) {

    Scanner ler = new Scanner(System.in);

    Calculadora calculadora = new Calculadora();

    int escolha;
    
    do{
      System.out.print("Escolha a operação desejada: \n");
      System.out.print("1 - Soma \n");
      System.out.print("2 - Subtração \n");
      System.out.print("3 - Multiplicação \n");
      System.out.print("4 - Divisão \n");
      escolha = ler.nextInt();
    }while(escolha < 1 || escolha > 4);

    switch(escolha){
      case 1:
        calculadora.setValor1(ler.nextDouble());
        calculadora.setValor2(ler.nextDouble());
        calculadora.Soma();
      break;

      case 2:
        calculadora.setValor1(ler.nextDouble());
        calculadora.setValor2(ler.nextDouble());
        calculadora.Subtração();
      break;

      case 3:
        calculadora.setValor1(ler.nextDouble());
        calculadora.setValor2(ler.nextDouble());
        calculadora.Multiplicação();
      break;

      case 4:
        calculadora.setValor1(ler.nextDouble());
        calculadora.setValor2(ler.nextDouble());
        calculadora.Divisão();;
      break;
    }

  }
}