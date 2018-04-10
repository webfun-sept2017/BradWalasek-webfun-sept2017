using System.ComponentModel.DataAnnotations;
namespace wedding_planner.Models
{
    public class RegisterViewModel
    {
        [Key]
        public int userid{get;set;}
        [Required]
        [MinLength(3)]
        public string firstname{get;set;}
        [Required]
        [MinLength(3)]
        public string lastname{get;set;}
        [Required]
        [EmailAddress]
        public string email{get;set;}
        [Required]
        [MinLength(8)]
        public string password{get;set;}
        [Compare("password")]
        public string confpassword{get;set;}
    }
}