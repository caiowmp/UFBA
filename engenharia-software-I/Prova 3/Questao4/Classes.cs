using System;

namespace Questao4
{
    public abstract class Sorvete
    {
        private double preco = -1;
        private string descricao = "Sorvete Abstrato.";
        
        public virtual double getPreco
        {
            get { return preco; }
        }
        public virtual string getDescricao
        {
            get { return descricao; }
        }
    }

    public abstract class Acompanhamento : Sorvete
    {
        double preco = -1;
        string descricao = "Acompanhamento do Sorvete";

        public override double getPreco
        {
            get { return preco; }
        }
        public override string getDescricao
        {
            get { return descricao; }
        }
    }

    class SorveteSimples : Sorvete
    {
        double preco = 5.00;
        string descricao = "Sorvete, ";

        public override double getPreco
        {
            get { return preco; }
        }
        public override string getDescricao
        {
            get { return descricao; }
        }
    }

    class Passas : Acompanhamento
    {
        double preco = 1.50;
        string descricao = "passas, ";
        Sorvete _Sorvete;

        public Passas(Sorvete Sorvete)
        {
            _Sorvete = Sorvete;
        }

        public override double getPreco
        {
            get { return _Sorvete.getPreco + preco; }
        }

        public override string getDescricao
        {
            get { return _Sorvete.getDescricao + descricao; }
        }
    }

    public class Calda : Acompanhamento
    {
        double preco = 1.00;
        string descricao = "calda, ";
        Sorvete _Sorvete;

        public Calda(Sorvete Sorvete)
        {
            _Sorvete = Sorvete;
        }

        public override double getPreco
        {
            get { return _Sorvete.getPreco + preco; }
        }

        public override string getDescricao
        {
            get { return _Sorvete.getDescricao + descricao; }
        }
    }
}
