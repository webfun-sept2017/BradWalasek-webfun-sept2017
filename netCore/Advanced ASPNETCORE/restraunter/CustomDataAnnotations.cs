using System;
using System.ComponentModel.DataAnnotations;

namespace restraunter
{
    public class CurrentDateAttribute : ValidationAttribute
    {
        public CurrentDateAttribute(){}
        public override bool IsValid(object value)
        {
            var dt = (DateTime)value;
            if(dt <= DateTime.Now)
            {
                return true;
            }
            return false;
        }
    }
}