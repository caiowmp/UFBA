class Boletim{

  private String número;
  private String tipo;
  private String detalhamento;
  private String data;
  private String localização;
  private String nome_registrador;
  private String CPF_solictante;

  
  //Um boletim de ocorrência pode ser cadastrado informando todos os seus dados descritos no cenário;
  public Boletim(String número,String tipo,String detalhamento,String data,String localização,String nome_registrador,String CPF_solicitante){

    this.número = número;
    this.tipo = tipo;
    this.detalhamento = detalhamento;
    this.data = data;
    this.localização = localização;
    this.nome_registrador = nome_registrador;
    this.CPF_solictante = CPF_solicitante;

  }


  //Um boletim de ocorrência pode ser cadastrado informando o número do boletim de ocorrência, tipo de ocorrência, data, localização da ocorrência.
  public Boletim(String número,String tipo,String data,String localização){

    this.número = número;
    this.tipo = tipo;
    this.data = data;
    this.localização = localização;

  }

  public String getNúmero(){
    return número;
  }

  public void setNúmero(String número){
    this.número = número;
  }

  public String getTipo(){
    return tipo;
  }

  public void setTipo(String tipo){
    this.tipo = tipo;
  }

  public String getDetalhamento(){
    return detalhamento;
  }

  public void setDetalhamento(String detalhamento){
    this.detalhamento = detalhamento;
  }

  public String getData(){
    return data;
  }

  public void setData(String data){
    this.data = data;
  }

  public String getLocalização(){
    return localização;
  }

  public void setLocalização(String localização){
    this.localização = localização;
  }

  public String getNomeRegistrador(){
    return nome_registrador;
  }

  public void setNomeRegistrador(){
    this.nome_registrador = nome_registrador;
  }

  public String getCPFSolicitante(){
    return CPF_solictante;
  }

  public void setCPFSolicitante(){
    this.CPF_solictante = CPF_solictante;
  }
}
