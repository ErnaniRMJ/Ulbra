using System;
using SistemaCobrancas.Services;

namespace SistemaCobrancas.Presentation
{
    public class CustomerChargePresentation
    {
        CustomerServices customerService = new CustomerServices();
        ChargeServices chargeService = new ChargeServices();

        public void Menu()
        {
            string operador = String.Empty;
            
            while(operador != "0")
            {
                Console.WriteLine("digite 1 para adicionar um novo cliente");
                Console.WriteLine("digite 2 para listar todos os clientes");
                Console.WriteLine("digite 0 para sair da aplicação");

                operador = Console.ReadLine();

                switch (operador)
                {
                    case "0":
                        Environment.Exit(0);
                    break;

                    case "1":
                        Console.WriteLine("digite o nome do cliente");
                        string customerName = Console.ReadLine();
                        Console.WriteLine("digite o telefone do cliente");
                        string customerPhone = Console.ReadLine();

                        var response = customerService.AddCustomer(customerName, customerPhone);
                        Console.WriteLine(response);
                        Console.WriteLine("");
                    break;

                    case "2":
                        var response2 = customerService.ShowCustomers();  
                        Console.WriteLine(response2);
                        Console.WriteLine("");
                    break;

                }

            }
        }
    }
}