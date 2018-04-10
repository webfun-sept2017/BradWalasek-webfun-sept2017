using System.ComponentModel.DataAnnotations;
using System;
namespace restraunter.Models
{
    public class Review : BaseEntity
    {  
        [Key]
        public int reviewid {get;set;}
        [Required]
        public string restaurant{get;set;}
        [Required]
        [MinLength(10,ErrorMessage="Your review must be more than 10 characters!")]
        public string content{get;set;}
        [Required]
        public string reviewer{get;set;}
        [Required]
        public int stars{get;set;}
        [Required]
        [CurrentDate(ErrorMessage = "Date must be before or on today!")]
        public DateTime date_of_visit{get;set;}
    }
}