using System.Text;
using SistemaCobrancas.Data;
using SistemaCobrancas.Domain;

namespace SistemaCobrancas.Services
{
    public class CustomerServices
    {
        CustomerRepository customerRepository = new CustomerRepository();

        public string AddCustomer (string name, string phoneNumber)
        {
            var customerId = customerRepository.ListSize() + 1;
            customerRepository.Save(new Customer(customerId, name, phoneNumber));
            return "cliente adicionado com sucesso!";
        }

        public string ShowCustomers()
        {
            var builder = new StringBuilder();
            var customerList = customerRepository.GetAll();
            var nunmberOfCustomers = customerList.Count;

            if (nunmberOfCustomers == 0)
                return builder.Append("Lista Vazia!").ToString();
            else
                {
                   foreach(Customer customer in customerList)
                   {
                       builder.AppendLine("Id:" + customer.Id + "nome: " + customer.Name + "Telefone:" + customer.PhoneNumber);
                   }

                   return builder.ToString();
                }


        }

        
    }
}