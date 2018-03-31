using System.ComponentModel.DataAnnotations;
namespace login_and_registration.Models
{
    public class User : BaseEntity
    {
        [Required]
        [MinLength(2)]
        public string firstName {get;set;}
        [Required]
        [MinLength(2)]
        public string lastName {get;set;}
        [Required]
        [EmailAddress]
        public string email {get;set;}
        [Required]
        [MinLength(8)]
        public string password {get;set;}
        [Compare("password", ErrorMessage="Passwords Must Match")]
        public string passconf{get;set;}
    }
}