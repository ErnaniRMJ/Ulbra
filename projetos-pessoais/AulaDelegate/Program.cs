using System.Globalization;
using System;

namespace AulaDelegate
{
    class Program
    {
        static void Main(string[] args)
        {
            // int resultado = CalculaMedia(2, 6);

            // Console.WriteLine($"Media: {resultado}");

            // Console.ReadKey();

            // bool valorRetornado = CalculaSeNumeroEstaEntre100E1000(345);

            //int valorRetornado = VerificarSeNumeroMaiorQue30(28);

            string valorRetornado = VerificarSe3NumerosMaior50(15, 25, 10);

            //int valorRetornado = VerificaSeSoma2NumerosMaior20(9, 10);

            //string valorRetornado = identificarSeSexoFeminino(20,"f",24);

            //double valorRetornado = consumoEstimado(190, "C");

            //string valorRetornado = validacaoSenha("1325");

            Console.WriteLine(valorRetornado);
        }


        //Calcacular a média entre dois números
        static int CalculaMedia(int parametro1, int parametro2)
        {
            int media;
            media = (parametro1 + parametro2) / 2;
            return media;
        }

        //Calcular a multiplicação entre dois números
        static int CalculaMultiplicacao(int parametro1, int parametro2)
        {
            int resultMultiplicacao = parametro1 * parametro2;
            return resultMultiplicacao;
        }

        /*Faça um algoritmo para ler um número e informar se ele está na 
        faixa de números entre 100(inclusive) e 1000(inclusive).*/
        static bool CalculaSeNumeroEstaEntre100E1000(int numero) {
            if (numero >= 100 && numero <= 1000)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        /*Faça um algoritmo para ler um número e se ele for maior do que 30, então
        exibir metade do número, caso contrário, imprimir o dobro do número.*/
        static int VerificarSeNumeroMaiorQue30(int numero)
        {
            if (numero > 30)
            {
                return 30 / 2;
            }
            else
            {
                return 30 * 2;
            }
        }

        /*Faça um algoritmo para ler três números e verificar se a soma deles é maior
        que 50. Se for, escrever uma mensagem informando.*/
        static string VerificarSe3NumerosMaior50(int numero1, int numero2, int numero3)
        {
            int resultadoSoma = (numero1 + numero2 + numero3);

            if (resultadoSoma > 50)
            {
                return "O número é maior que 50";
            }
            else
            {
                return "O número é menor ou igual a 50";
            }
        }

        /*Construa um algoritmo que leia dois números e efetue a adição. Caso o valor
        somado seja maior que 20, este deverá ser apresentado somando e a ele mais
        8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado
        subtraindo-se 5*/

        static int VerificaSeSoma2NumerosMaior20(int numero1, int numero2)
        {
            int resultadoValor = numero1 + numero2;

            if (resultadoValor > 20)
            {
                return resultadoValor + 8;
            }
            else
            {
                return resultadoValor - 5;
            }
        }

        /*Faça um algoritmo para entrar com código, sexo e idade de uma pessoa. Se a
        pessoa for do sexo feminino e tiver menos que 25 anos, imprimir código e
        mensagem: ACEITA. Caso contrário, imprimir código e a mensagem: NÃO
        ACEITA.*/
        static string identificarSeSexoFeminino(int codigo, string sexo, int idade)
        {
            if((sexo == "F" || sexo == "f") && idade < 25)
            {
                return "PESSOA CODIGO " + codigo + " ACEITA";
            }
            else
            {
                return "PESSOA CODIGO " + codigo + " NAO ACEITA";
            }
        }

        /*Fazer um algoritmo que leia o percurso em quilômetros, o tipo do carro e
        informe o consumo estimado de combustível, sabendo-se que um carro tipo C
        faz 12 Km com um litro de gasolina, um tipo B faz 9 Km e o tipo A, 8 Km por
        litro.*/

        static double consumoEstimado(int distancia, string tipoCarro)
        {
            if (tipoCarro == "A" || tipoCarro =="a")
            {
                var litrosConsumidos = distancia / 8;
                return litrosConsumidos;
            }
            
            if (tipoCarro == "B" || tipoCarro =="b")
            {
                var litrosConsumidos = distancia / 9;
                return litrosConsumidos;
            }
            if (tipoCarro == "C" || tipoCarro =="c")
            {
                var litrosConsumidos = distancia / 12;
                return litrosConsumidos;
            } 
            else
            {
                return 0;
            }
        }

        /*Faça um algoritmo que verifique a validade de uma senha fornecida pelo
        usuário. A senha válida é o número 1234. OBS: Se a senha informada
        pelo usuário for inválida, a mensagem &quot;ACESSO NEGADO&quot; deve ser exibida.
        Se for a correta, a mensagem "ACESSO PERMITIDO" deverá ser exibida.*/

        static string validacaoSenha(string senha)
        {
            if(senha == "1234")
            {
                return "ACESSO PERMITIDO";
            }
            else
            {
                return "ACESSO NEGADO";
            }
        }

        /*As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e
        R$ 1,00 se forem compradas pelo menos 12. Escreva um algoritmo que leia o
        número de maçãs compradas, calcule e escreva o custo total da compra.*/

        /*Faça um algoritmo para ler o codigo de 2 times e o número de gols marcados
        na partida (para cada time). Escrever o codigo do vencedor. Caso não haja
        vencedor deverá ser impressa a palavra EMPATE.*/

        /*Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
        Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
        Também testar se saldo atual for maior ou igual a zero escrever a mensagem
        &#39;Saldo Positivo&#39;, senão escrever a mensagem &#39;Saldo Negativo&#39;.*/

        /*Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima
        em estoque e quantidade mínima em estoque de um produto. Calcular e
        escrever a quantidade média ((quantidade média = quantidade máxima +
        quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a
        quantidade média escrever a mensagem &#39;Não efetuar compra&#39;, senão escrever
        a mensagem &#39;Efetuar compra&#39;.*/
    }
}
