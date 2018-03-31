using System.ComponentModel.DataAnnotations;
namespace dojo_league.Models
{
    public class Ninja : BaseEntity
    {
        [Key]
        public long id{get;set;}
        [Required]
        [MinLength(3)]
        public string name{get;set;}
        [Required]
        public int level {get;set;}
        public string description{get;set;}
        [Required]
        public Dojo dojo{get;set;}
    }
}