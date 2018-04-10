using Microsoft.EntityFrameworkCore;

namespace restraunter.Models
{
    public class Context : DbContext
    {
        public Context(DbContextOptions<Context> options) : base(options){}
        public DbSet<Review> reviews{get;set;}
    }
}