using System.Collections.Generic;
namespace bank_accounts.Models
{
    public class User : BaseEntity
    {
        public int userid{get;set;}
        public string firstname{get;set;}
        public string lastname{get;set;}
        public string email{get;set;}
        public string password{get;set;}
        public List<Transaction> Transactions{get;set;}
        public User()
        {
            Transactions = new List<Transaction>();
        }
    }
}