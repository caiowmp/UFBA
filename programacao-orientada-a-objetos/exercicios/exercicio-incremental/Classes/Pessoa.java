package Classes;

import java.util.Date;
import java.util.Calendar;

public abstract class Pessoa{

  protected String nome;
  protected String tipo;
  protected String cpf_cnpj;
  protected Date dataNascimento = new Date();
  protected String rua;
  protected String complemento;
  protected String bairro;
  protected Integer numero;
  protected Integer idade;

  protected Pessoa(String nome,String tipo,String cpf_cnpj,Date dataNascimento,String rua,String complemento,String bairro,Integer numero){
    this.nome = nome;
    this.tipo = tipo;
    this.cpf_cnpj = cpf_cnpj;
    this.dataNascimento = dataNascimento;
    this.rua = rua;
    this.complemento = complemento;
    this.bairro = bairro;
    this.numero = numero;
  }

  public void setNome(String nome){
    this.nome = nome;
  }

  public String getNome(){
    return nome;
  }

  public void setTipo(String tipo){
    this.tipo = tipo;
  }

  public String getTipo(){
    return tipo;
  }

  public void setCpf_Cnpj(String cpf_cnpj){
    this.cpf_cnpj = cpf_cnpj;
  }

  public String getCpf_Cnpj(){
    return cpf_cnpj;
  }

  public void setDataNascimento(Date dataNascimento){
    this.dataNascimento = dataNascimento;
  }

  public Date getDataNascimento(){
    return dataNascimento;
  }

  public void setRua(String rua){
    this.rua = rua;
  }

  public String getRua(){
    return rua;
  }

  public void setComplemento(String complemento){
    this.complemento = complemento;
  }

  public String getComplemento(){
    return complemento;
  }

  public void setBairro(String bairro){
    this.bairro = bairro;
  }

  public String getBairro(){
    return bairro;
  }

  public void setNumero(Integer numero){
    this.numero = numero;
  }

  public Integer getNumero(){
    return numero;
  }

  public String VerificaPessoa(){
		
    return getTipo();
	}
	
	public Integer getIdade() {
		Calendar data_Nascimento = Calendar.getInstance();
		Calendar dataAtual = Calendar.getInstance();

		data_Nascimento.setTime(dataNascimento);
		
		Integer diferencaMes = dataAtual.get(Calendar.MONTH) - data_Nascimento.get(Calendar.MONTH);
		Integer diferencaDia = dataAtual.get(Calendar.DAY_OF_MONTH) - data_Nascimento.get(Calendar.DAY_OF_MONTH);
		Integer idade = (dataAtual.get(Calendar.YEAR) - data_Nascimento.get(Calendar.YEAR));

		if(diferencaMes < 0 || (diferencaMes == 0 && diferencaDia < 0)) {
			idade--;
		}

		return idade;
	}
}