namespace lost_in_the_woods
{
    public class Trail : BaseEntity
    {
        public string name{get;set;}
        public int length{get;set;}
        public int elevation{get;set;}
        public float latitude{get;set;}
        public float longitude{get;set;}
        public string description{get;set;}
    }
}