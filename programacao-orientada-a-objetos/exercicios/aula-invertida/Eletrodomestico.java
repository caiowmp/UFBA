abstract class Eletrodomestico{

  protected String nome;
  protected boolean status;

  protected Eletrodomestico(String nome){
    this.nome = nome;
    status = false;
  }

  protected void LigaDesliga(){

    if(status){
      status = false;
    }else{
      status = true;
    }
  }

}