class Doação{

  private Doador doador;
  private String tipo_doacao;
  private String descrição_doacao;
  private String estado_doacao;
  private Integer quantidade = 0;
  private boolean pode_ser_entregue;
  private String tamanho_doacao;

  public Doação(Doador doador,String tipo_doacao,String descrição_doacao,String estado_doacao,Integer quantidade,boolean pode_ser_entregue){

    this.doador = doador;
    this.tipo_doacao = tipo_doacao;
    this.descrição_doacao = descrição_doacao;
    this.estado_doacao = estado_doacao;
    this.quantidade = quantidade;
    this.pode_ser_entregue = pode_ser_entregue;
  }

  public void setDoador(Doador doador){
    this.doador = doador;
  }

  public Doador getDoador(){
    return doador;
  }

  public void setTipoDoacao(String tipo_doacao){
    this.tipo_doacao = tipo_doacao;
  }

  public String getTipoDoacao(){
    return tipo_doacao;
  }

  public void setDescriçãoDoacao(String descrição_doacao){
    this.descrição_doacao = descrição_doacao;
  }

  public String getDescriçãoDoacao(){
    return descrição_doacao;
  }

  public void setEstadoDoacao(String estado_doacao){
    this.estado_doacao = estado_doacao;
  }

  public String getEstadoDoacao(){
    return estado_doacao;
  }

  public Integer getQuantidade(){
    return quantidade;
  }

  public void setQuantidade(Integer quantidade){
    this.quantidade = quantidade;
  }

  public boolean getPodeSerEntregue(){
    return pode_ser_entregue;
  }

  public void setPodeSerEntregue(boolean pode_ser_entregue){
    this.pode_ser_entregue = pode_ser_entregue;
  }


  // Item 4
  public void setTamanhoDoacao(){
    
    if(this.quantidade < 10){
      this.tamanho_doacao = "Pequena";
    }else if(this.quantidade < 30){
      this.tamanho_doacao = "Média";
    }else{
      this.tamanho_doacao = "Grande";
    }

    System.out.println("Essa doação é " + this.tamanho_doacao);
  }

}