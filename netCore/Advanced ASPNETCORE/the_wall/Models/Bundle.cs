using System.Collections.Generic;
namespace the_wall.Models
{
    public class Bundle : BaseEntity
    {
        public string name {get;set;}
        public List<Dictionary<string,object>> messages{get;set;}
        public List<Dictionary<string,object>> comments{get;set;}
    }
}