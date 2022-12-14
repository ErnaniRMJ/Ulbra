using System;
using System.Collections.Generic;
using SistemaCobrancas.Domain;

namespace SistemaCobrancas.Data
{
    public class ChargeRepository
    {
        private List<Charge> billingList = new List<Charge>();
        
        public void  Save(Charge charge)
        {
            billingList.Add(charge);

        }
        public Charge GetById(int chargeId)
        {
             return billingList.Find(x=> x.Id == chargeId);
        }
         public void Update(Charge charge)
        {
            charge.PaymentDate = DateTime.Now;
            charge.Status = true;
        }

        public bool Delete (int chargeId)
        {
            var charge = billingList.Find(x=> x.Id == chargeId);

            if (charge == null)
               return false;
            else 
            {
                billingList.Remove(charge);
               return true;
            }   
        }

        public List<Charge> GetAll ()
        {
            return billingList;
        }
        
        public int ListSize()
        {
            return billingList.Count;
        }
    
        public List<Charge> GetAllCustomerCharges(int customerId)
        {
            var CustomerCharges = billingList.FindAll(x => x.Customer.Id == customerId);
            return CustomerCharges;
        }
    }
        
       
}