class Conta{ // Sempre que colo public class da erro na hora de compilar '-'

  private String nome;
  private int numeroConta;
  private double saldo;

  public Conta(String nome, int numeroConta,double saldo){
    this.nome = nome;
    this.numeroConta = numeroConta;
    this.saldo = saldo;
  }

  public void setNome(String nome){
    this.nome = nome;
  }

  public String getNome(){
    return nome;
  }

  public void setNumeroConta(int numeroConta){
    this.numeroConta = numeroConta;
  }

  public int getNumeroConta(){
    return numeroConta;
  }

  public void setSaldo(double saldo){
    this.saldo = saldo;
  }

  public double getSaldo(){
    return saldo;
  }
    
  public void Depositar(double depósito){
    saldo = saldo + depósito;
  }

  public void Sacar(double saque){
    saldo = saldo - saque;
  }
}

public class Main {
  public static void main(String[] args) {

    Conta conta = new Conta("Caio",447653,55.88);

  }
}