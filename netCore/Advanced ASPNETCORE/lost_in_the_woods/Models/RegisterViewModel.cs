using System.ComponentModel.DataAnnotations;

namespace lost_in_the_woods
{
    public class RegisterViewModel : BaseEntity
    {
        [Required]
        public string name{get;set;}
        [Required]
        [Range(0, int.MaxValue, ErrorMessage="Please enter a number(0 if trail length is unknown)")]
        public int length{get;set;}
        [Required]
        [Range(0, int.MaxValue, ErrorMessage="Please enter a number(0 if elevation change is unknown)")]
        public int elevation{get;set;}
        [Required]
        [Range(0, float.MaxValue, ErrorMessage="Please enter a number(0 if latitude change is unknown)")]
        public float latitude{get;set;}
        [Required]
        [Range(0, float.MaxValue, ErrorMessage="Please enter a number(0 if longitude change is unknown)")]
        public float longitude{get;set;}
        [MinLength(10)]
        public string description{get;set;}
    }
}