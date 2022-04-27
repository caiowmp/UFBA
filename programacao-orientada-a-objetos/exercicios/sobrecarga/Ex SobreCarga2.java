class Lâmpada{ // Sempre que colo public class da erro na hora de compilar '-'

  private String tipo;
  private String estado; // ia fazer com boolean mas na hora de passar o estado é mais fácil por dizendo se está ligado ou desligado do que true or false.
  private int potência;

  public Lâmpada(){
    tipo = "Led";
    estado = "Ligado";
    potência = 60;
  }

  public Lâmpada(String tipo, String estado, int potência){
    this.tipo = tipo;
    this.estado = estado;
    this.potência = potência;
  }

  public String getTipo(){
    return tipo;
  }

  public String getEstado(){
    return estado;
  }

  public int getPotência(){
    return potência;
  }
}

public class Main {
  public static void main(String[] args) {

    Lâmpada lâmpada1 = new Lâmpada();

    System.out.print("Tipo: " + lâmpada1.getTipo() + ". ");
    System.out.print("Estado: " + lâmpada1.getEstado() + ". ");
    System.out.print("Potência: " + lâmpada1.getPotência());

    System.out.print("\n");

    Lâmpada lâmpada2 = new Lâmpada("Fluorescente","Desligada",120);

    System.out.print("Tipo: " + lâmpada2.getTipo() + ". ");
    System.out.print("Estado: " + lâmpada2.getEstado() + ". ");
    System.out.print("Potência: " + lâmpada2.getPotência());
  }
}