class Ventilador extends Eletrodomestico{

  public Ventilador(){
    super("Ventilador");
  }

  public void LigaDesliga(){

    super.LigaDesliga();

    if(status){
      System.out.println("O Ventilador foi ligado");
    }else{
      System.out.println("O Ventilador foi desligado");
    }

  }

}