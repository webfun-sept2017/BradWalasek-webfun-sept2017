namespace testing_ground
{
    public class Person
    {
        public string name {get;set;}
        public string home {get;set;}
        public int age {get;set;}
        public string fullname{
            get {return $"{name} from {home} at the age of {age}";}
        }

    }
}