using System.ComponentModel.DataAnnotations;

namespace bank_accounts.Models
{
    public class RegisterViewModel : BaseEntity
    {
        [Key]
        public int userid{get;set;}
        [Required(ErrorMessage="Must fill out a first name")]
        [MinLength(3)]
        public string firstname{get;set;}
        [Required(ErrorMessage="Must fill out a last name")]
        [MinLength(3)]
        public string lastname{get;set;}

        [Required(ErrorMessage="Must fill out an Email address")]
        [EmailAddress]
        public string email{get;set;}

        [Required(ErrorMessage="Must enter a password")]
        [MinLength(8,ErrorMessage="Password must be more than 8 characters")]
        public string password{get;set;}

        [Required(ErrorMessage="Must fill in confirm password field")]
        [Compare("password",ErrorMessage="Passwords must match")]
        public string passwordconfirm{get;set;}
    }
}