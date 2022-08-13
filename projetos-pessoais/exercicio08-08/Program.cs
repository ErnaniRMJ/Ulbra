using System;

namespace exercicio08_08
{
    class Program
    {
        static void Main(string[] args)
        {
            double retornoDaMinhaFuncao = DescontoDeVendas()
            Console.WriteLine(retornoDaMinhaFuncao);
        }

        static double DescontoDeVendas(double valorVenda)
        {
            Console.WriteLine("1 - venda avista");
            Console.WriteLine("2 - venda a prazo 30 dias");
            Console.WriteLine("3 - venda a prazo 60 dias");
            Console.WriteLine("4 - venda a prazo 90 dias");
            Console.WriteLine("5 - venda cartao debito");
            Console.WriteLine("6 - venda cartao credito");
            string valorDigitadoUsuario = Console.ReadLine();

            if(valorDigitadoUsuario == "1")
            {
                double desconto = valorVenda/10;
                double total = valorVenda - desconto;
                return total;             
            }
            else if(valorDigitadoUsuario == "2")
            {
                double desconto = (valorVenda/100)*5;
                double total = valorVenda - desconto;
                return total;
            }
            else if(valorDigitadoUsuario == "3")
            {
                return valorVenda;
            }
            else if(valorDigitadoUsuario == "4")
            {
                double acrecimo = (valorVenda/100)*5;
                double total = valorVenda + acrecimo;
                return total;
            }
            else if (valorDigitadoUsuario == "5")
            {
                double desconto = (valorVenda/100)*8;
                double total = valorVenda - desconto;
                return total; 
            }
            else if (valorDigitadoUsuario == "6")
            {
                 double desconto = (valorVenda/100)*7;
                double total = valorVenda - desconto;
                return total;
            }
            else
            {
                return 0;
            }
        
        }
    }

    /*13 - Faça um programa que receba o valor da venda, escolha a condição de
pagamento no menu e mostre o total da venda final conforme condições a
seguir:
1 - Venda a Vista - desconto de 10%
2 - Venda a Prazo 30 dias - desconto de 5%
3 - Venda a Prazo 60 dias - mesmo preço
4 - Venda a Prazo 90 dias - acréscimo de 5%
5 - Venda com cartão de débito - desconto de 8%
6 - Venda com cartão de crédito - desconto de 7%*/
}
