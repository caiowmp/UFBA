class Linha{ // Sempre que colo public class da erro na hora de compilar '-'

  private double[] Coordenadas = new double[4];

  public Linha(double x1,double y1,double x2,double y2){
    Coordenadas[0] = x1;
    Coordenadas[1] = y1;
    Coordenadas[2] = x2;
    Coordenadas[3] = y2;
  }

  public Linha(double x2,double y2){
    Coordenadas[0] = 0;
    Coordenadas[1] = 0;
    Coordenadas[2] = x2;
    Coordenadas[3] = y2;
  }

  public double[] getCoordenadas(){
    return Coordenadas;
  }

}

public class Main {
  public static void main(String[] args) {

    Linha linha1 = new Linha(1,2,3,4);

    for(double i : linha1.getCoordenadas()){
      System.out.print(i + " ");
    }

    System.out.print("\n");

    Linha linha2 = new Linha(1,2);

    for(double j : linha2.getCoordenadas()){
      System.out.print(j + " ");
    }
  }
}