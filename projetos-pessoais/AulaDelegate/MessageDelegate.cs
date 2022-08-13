using System;

namespace AulaDelegate
{
    public class MessageDelegate
    {
        public void Mensagem1()
        {

            string MinhaMensagem1() => "Mensagem 1 - Sextou!";
            var mensagemCompleta = ObterMensagem(MinhaMensagem1);
            Console.WriteLine(mensagemCompleta);
        }

        public void Mensagem2()
        {
            string MinhaMensagem2() => "Mensagem 2 - Bora pro bar";

            var mensagemCompleta = ObterMensagem(MinhaMensagem2);
            Console.WriteLine(mensagemCompleta);
        }

        public void Mensagem3()
        {
            string MinhaMensagem3() => "Mensagem 3 - beber!";

            var mensagemCompleta = ObterMensagem(MinhaMensagem3);
            Console.WriteLine(mensagemCompleta);
        }
        public delegate string ObterMensagemEspecifica();

        private string ObterMensagem(ObterMensagemEspecifica mensagemEspecifica)
        {
            string mensagem = string.Empty;
            mensagem += "Inicio da mensagem\r\n\r\n";
            mensagem += mensagemEspecifica();
            mensagem += "\r\n\r\n";
            mensagem += "Final da mensagem\r\n";
            mensagem += "-------------------------------\r\n";

            return mensagem;
        }
    }
}