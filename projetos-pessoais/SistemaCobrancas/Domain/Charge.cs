using System;

namespace SistemaCobrancas.Domain
{
    public class Charge
    {
        public Charge(int id, DateTime DueDate, double amountCharge, Customer customer)
        {
          this.Id = id;
          this.IssuanceDate = DateTime.Now;
          this.DueDate = DueDate;
          this.AmountCharge = amountCharge;
          this.PaymentDate = null;
          this.Status = false;
          this.Customer = customer;
        }
     public int Id { get; set; } 
     public DateTime IssuanceDate { get; set; } //Data de Emissao
     public DateTime DueDate { get; set; } //Data de vencimento
     public double AmountCharge { get; set; } //Valor da cobranca
     public DateTime? PaymentDate { get; set; } //DataPagamento
     public bool Status { get; set; } //Status do Pagamento
     public Customer Customer { get; private set; }
     
    }
}