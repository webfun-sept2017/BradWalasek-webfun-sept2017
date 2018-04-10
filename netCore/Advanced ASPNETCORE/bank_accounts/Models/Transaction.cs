using System;
namespace bank_accounts.Models
{
    public class Transaction : BaseEntity
    {
        public int transactionid{get;set;}
        public float amount{get;set;}
        public int userid{get;set;}
        public User user{get;set;}
        public DateTime created_on {get;set;}
    }
}