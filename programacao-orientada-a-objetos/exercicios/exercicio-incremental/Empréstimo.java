class Empréstimo{

  private Beneficiário beneficiário;
  private String tipo_emprestimo;
  private String descrição_emprestimo;
  private Integer quantidade;

  public Empréstimo(Beneficiário beneficiário,String tipo_emprestimo,String descrição_emprestimo,Integer quantidade){

    this.beneficiário = beneficiário;
    this.tipo_emprestimo = tipo_emprestimo;
    this.descrição_emprestimo = descrição_emprestimo;
    this.quantidade = quantidade;
  }

  public Beneficiário getBeneficiário(){
    return beneficiário;
  }

  public void setBeneficiário(Beneficiário beneficiário){
    this.beneficiário = beneficiário;
  }

  public String getTipoEmprestimo(){
    return tipo_emprestimo;
  }

  public void setTipoEmprestimo(String tipo_emprestimo){
    this.tipo_emprestimo = tipo_emprestimo;
  }

  public String getDescriçãoEmprestimo(){
    return descrição_emprestimo;
  }

  public void setDescriçãoEmprestimo(String descrição_emprestimo){
    this.descrição_emprestimo = descrição_emprestimo;
  }

  public Integer getQuantidade(){
    return quantidade;
  }

  public void setQuantidade(Integer quantidade){
    this.quantidade = quantidade;
  }
}


