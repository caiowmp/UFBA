class Emprestimo{

  private Beneficiario beneficiario;
  private String tipo_emprestimo;
  private String descrição_emprestimo;
  private Integer quantidade;

  public Emprestimo(Beneficiario beneficiário,String tipo_emprestimo,String descrição_emprestimo,Integer quantidade){

    this.beneficiario = beneficiario;
    this.tipo_emprestimo = tipo_emprestimo;
    this.descrição_emprestimo = descrição_emprestimo;
    this.quantidade = quantidade;
  }

  public Beneficiario getbeneficiario(){
    return beneficiario;
  }

  public void setbeneficiario(Beneficiario beneficiario){
    this.beneficiario = beneficiario;
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


