package Classes;

import java.util.Date;

public class Beneficiario extends Pessoa{
  
  public Beneficiario(String nome,String tipo,String cpf_cnpj,Date dataNascimento,String rua,String complemento,String bairro,Integer numero){

    super(nome,tipo,cpf_cnpj,dataNascimento,rua,complemento,bairro,numero);
  }

 public String VerificaPessoa(){
    if(super.VerificaPessoa() == "Pessoa Física"){
      return "Beneficiário é uma pessoa Física";
    }else{
      return "Beneficiário é uma pessoa Jurídica";
    }
	}

}