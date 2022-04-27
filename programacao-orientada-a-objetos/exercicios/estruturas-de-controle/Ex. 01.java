class Pessoa{ // Sempre que colo public class da erro na hora de compilar '-'

  private String nome;
  private int[] Nascimento = new int[3];
  private double altura;
  public int idade;

  public Pessoa(){}

  public void setNome(String nome){
    this.nome = nome;
  }

  public String getNome(){
    return nome;
  }

  public void setNascimento(int anoNascimento, int mesNascimento, int diaNascimento){
    Nascimento[0] = diaNascimento;
    Nascimento[1] = mesNascimento;
    Nascimento[2] = anoNascimento;
  }

  public int[] getNascimento(){
    return Nascimento;
  }

  public void setAltura(double altura){
    this.altura = altura;
  }

  public double getAltura(){
    return altura;
  }
    
  public void info(){
    System.out.print("Nome: " + nome +"\nNascimento: " + Nascimento[2]+"/"+Nascimento[1]+"/"+Nascimento[0] +"\nAltura: " + altura);
  }

  public void idade(){
    if(Nascimento[1] < 9){
      idade = 2021 - Nascimento[0];
    }else{
      if(Nascimento[2] <= 06){
        idade = 2021 - Nascimento[0];
      }else{
        idade = 2020 - Nascimento[0];
      }
    }
  }
}

public class Main {
  public static void main(String[] args) {

    Pessoa pessoa01 = new Pessoa();

    pessoa01.setNome("Caio");
    pessoa01.setNascimento(26,07,2005);
    pessoa01.setAltura(1.85);

    pessoa01.info();

  }
}