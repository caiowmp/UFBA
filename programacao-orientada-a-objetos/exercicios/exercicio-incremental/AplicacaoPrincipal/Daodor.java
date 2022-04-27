package AplicacaoPrincipal;
import Classes.*;

import java.util.Date;

class Doador extends Pessoa{

  public Doador(String nome,String tipo,String cpf_cnpj,Date dataNascimento,String rua,String complemento,String bairro,Integer numero){

    super(nome,tipo,cpf_cnpj,dataNascimento,rua,complemento,bairro,numero);
  }

  public String VerificaPessoa(){
    if(super.VerificaPessoa() == "Pessoa Física"){
      return "Doador é uma pessoa Física";
    }else{
      return "Doador é uma pessoa Jurídica";
    }
	}

}