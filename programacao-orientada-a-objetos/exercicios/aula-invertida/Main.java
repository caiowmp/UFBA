class Main{
  public static void main(String[] args) {

    Eletrodomestico aparelho1 = new Televisao();

    aparelho1.LigaDesliga();
    aparelho1.LigaDesliga();

    Eletrodomestico aparelho2 = new Ventilador();

    aparelho2.LigaDesliga();
    aparelho2.LigaDesliga();
  }
}
