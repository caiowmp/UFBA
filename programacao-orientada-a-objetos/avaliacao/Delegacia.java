import java.util.ArrayList;

class Delegacia{

  private String nome;
  private String CNPJ;
  private String endereço;
  private String nome_delegado;
  private boolean status; 
  //"uma lista de boletins de ocorrência é registrada na delegacia."
  private ArrayList<Boletim>boletins;


  //Uma delegacia pode ser cadastrada informando todos os dados descritos no cenário;
  public Delegacia(String nome,String CNPJ, String endereço,String nome_delegado, boolean status){

    this.nome = nome;
    this.CNPJ = CNPJ;
    this.endereço = endereço;
    this.nome_delegado = nome_delegado;
    this.status = status;
    //A lista de boletins de ocorrência registrados na delegacia deve estar vazia neste momento.
    this.boletins = new ArrayList<Boletim>();

  }

  //caso não seja informado o status, considerar o status como inativa
  public Delegacia(String nome,String CNPJ, String endereço,String nome_delegado){

    this.nome = nome;
    this.CNPJ = CNPJ;
    this.endereço = endereço;
    this.nome_delegado = nome_delegado;
    this.status = false;
    //A lista de boletins de ocorrência registrados na delegacia deve estar vazia neste momento.
    this.boletins = new ArrayList<Boletim>();

  }

  public String getNome(){
    return nome;
  }

  public void setNome(String nome){
    this.nome = nome;
  }

  public String getCNPJ(){
    return CNPJ;
  }

  public void setCNPJ(String CNPJ){
    this.CNPJ = CNPJ;
  }

  public String getEndereço(){
    return endereço;
  }

  public void setEndereço(String endereço){
    this.endereço = endereço;
  }

  public String getNomeDelegado(){
    return nome_delegado;
  }

  public void setNomeDelegado(String nome_delegado){
    this.nome_delegado = nome_delegado;
  }

  public boolean getStatus(){
    return status;
  }

  public void setStatus(boolean status){
    this.status = status;
  }

  //Um método que permita que um boletim de ocorrência seja adicionado à lista BOs de uma delegacia.
  public boolean addBoletim(String número,String tipo,String detalhamento,String data,String localização,String nome_registrador,String CPF_solicitante){

    boolean aux = true;

    //(Lembre-se de verificar se esse BO já está na lista, não será permitido duplicatas
    for(Boletim i : boletins){
      if(i.getNúmero() == número){
        aux = false;
      }
    }

    if(aux){
      boletins.add(new Boletim(número,tipo,detalhamento,data,localização,nome_registrador,CPF_solicitante));
    }

    return aux;
    
  }


  //Um método que permita que um boletim de ocorrência seja adicionado à lista BOs de uma delegacia.
  public boolean addBoletim(String número,String tipo,String data,String localização){
    
    boolean aux = true;

    //(Lembre-se de verificar se esse BO já está na lista, não será permitido duplicatas
    for(Boletim i : boletins){
      if(i.getNúmero() == número){
        aux = false;
      }
    }

    if(aux){
      boletins.add(new Boletim(número,tipo,data,localização));
    }

    return aux;
  }

  //recebe o número do  boletim de ocorrência como parâmetro;
  public boolean removeBoletim(String número){

    boolean aux = false;

    for(int i = 0; i < boletins.size(); i++){
      if(boletins.get(i).getNúmero() == número){
        boletins.remove(i);
        aux = true;
      }
    }

    return aux;

  }

  //recebe uma instância de um boletim de ocorrência
  public boolean removeBoletim(Boletim boletim){

    boolean aux = false;

    for(int i = 0; i < boletins.size(); i++){
      if(boletins.get(i) == boletim){
        boletins.remove(i);
        aux = true;
      }
    }

    return aux;

  }


  //imprimir os dados da delegacia e a quantidade de boletins (sem parâmetros de entrada)
  public void imprimeBoletins(){

    System.out.println("Dados da Delegacia:" + "\nNome: "+ this.nome + "\nCNPJ: " + this.CNPJ + "\nEndereço: " + this.endereço + "\nNome do delegado: " + this.nome_delegado + "\nStatus: ativa");

    System.out.println("\nQuantidade de boletins: " + boletins.size());

  }

  public void imprimeBoletins(boolean status){

    if(status == this.status){
      System.out.println("Dados da Delegacia:" + "\nNome: "+ this.nome + "\nCNPJ: " + this.CNPJ + "\nEndereço: " + this.endereço + "\nNome do delegado: " + this.nome_delegado);

      for(int i = 0; i<boletins.size(); i++){
        System.out.println("\nDados dos boletins:" + "\nNúmero: " + boletins.get(i).getNúmero() + "\nTipo:" + boletins.get(i).getTipo() + "\nDetalhamento:" + boletins.get(i).getDetalhamento() + "\nData:" + boletins.get(i).getData() + "\nLocalização:" +boletins.get(i).getLocalização() + "\nNome do Registrador: " +boletins.get(i).getNomeRegistrador() + "\nCpf do solicitante: " + boletins.get(i).getCPFSolicitante());
      }
    }
  }

}




