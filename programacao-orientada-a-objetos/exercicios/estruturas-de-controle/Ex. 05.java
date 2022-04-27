class Fibonacci{ // Sempre que colo public class da erro na hora de compilar '-'

  private int n1 = 0;
  private int n2 = 1;
  private int n3;

  public Fibonacci(){}

  public void setN1(int n1){
    this.n1 = n1;
  }

  public int getN1(){
    return n1;
  }

  public void setN2(int n2){
    this.n2 = n2;
  }

  public int getN2(){
    return n2;
  }

  public void setN3(){
    n3 = n1 + n2;
  }

  public int getN3(){
    return n3;
  }

}

public class Main {
  public static void main(String[] args) {

    Fibonacci fib = new Fibonacci();

    do{
      fib.setN3();
      System.out.print(fib.getN1() + ",");
      fib.setN1(fib.getN2());
      fib.setN2(fib.getN3());
    }while(fib.getN1() < 145);

    System.out.print("etc");


  }
}