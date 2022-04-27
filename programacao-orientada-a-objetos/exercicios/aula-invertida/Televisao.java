class Televisao extends Eletrodomestico{

  public Televisao(){
    super("Televisão");
  }

  public void LigaDesliga(){

    super.LigaDesliga();

    if(status){
      System.out.println("A Televisão foi ligada");
    }else{
      System.out.println("A Televisão foi desligada");
    }

  }

}