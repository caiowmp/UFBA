using System;

namespace Questao4
{
    class SorveteMaker
    {
        static void Main(string[] args)
        {
            //criar um Sorvete
            Sorvete Sorvete = new SorveteSimples();
            //coloca calda no sorvete
            Sorvete = new Calda(Sorvete);
            Sorvete = new Calda(Sorvete);
            //coloca passas no sorvete
            Sorvete = new Passas(Sorvete);
            Console.WriteLine("Preco -->" + Sorvete.getPreco.ToString());
            Console.WriteLine("Descricao --> "+ Sorvete.getDescricao.TrimEnd(' ', ','));         
            Console.ReadLine();
        }
    }
}

