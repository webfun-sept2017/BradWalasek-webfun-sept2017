using Microsoft.EntityFrameworkCore;

namespace bank_accounts.Models
{
    public class Context : DbContext
    {
        public Context(DbContextOptions<Context> options) : base(options){}
        public DbSet<User> Users{get;set;}
        public DbSet<Transaction> Transactions{get;set;}
    }
}