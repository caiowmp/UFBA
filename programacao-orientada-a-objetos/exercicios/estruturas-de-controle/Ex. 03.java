import java.util.Scanner;

class Aluno{ // Sempre que colo public class da erro na hora de compilar '-'

  private String nome;
  private double nota1;
  private double nota2;
  private double nota3;
  private double média;
  private String resultado;

  public Aluno(){}

  public void setNome(String nome){
    this.nome = nome;
  }

  public String getNome(){
    return nome;
  }

  public void setNota1(double nota1){
    this.nota1 = nota1;
  }

  public double getNota1(){
    return nota1;
  }

  public void setNota2(double nota2){
    this.nota2 = nota2;
  }

  public double getNota2(){
    return nota2;
  }

  public void setNota3(double nota3){
    this.nota3 = nota3;
  }

  public double getNota3(){
    return nota3;
  }

  public void setMédia(){
    média = (nota1 + nota2 + nota3) / 3;
  }

  public void setResultado(){

    if(média >= 5){
      resultado = "Aprovado";
    }else{
      resultado = "Reprovado";
    }
  }

  public String getResultado(){
    return resultado;
  }

}

public class Main {
  public static void main(String[] args) {

    Scanner ler = new Scanner(System.in);

    Aluno aluno = new Aluno();

    System.out.print("Por favor, escreva seu Nome: ");
    aluno.setNome(ler.next());
    
    do{
      System.out.print("\nPor favor, escreva sua Nota1: ");
      aluno.setNota1(ler.nextDouble());
    }while(aluno.getNota1() < 0 || aluno.getNota1() > 10 );

    do{
      System.out.print("\nPor favor, escreva sua Nota2: ");
      aluno.setNota2(ler.nextDouble());
    }while(aluno.getNota2() < 0 || aluno.getNota2() > 10 );

    do{
      System.out.print("\nPor favor, escreva sua Nota3: ");
      aluno.setNota3(ler.nextDouble());
    }while(aluno.getNota3() < 0 || aluno.getNota3() > 10 );
    
    aluno.setMédia();
    aluno.setResultado();

    System.out.print(aluno.getResultado());

  }
}