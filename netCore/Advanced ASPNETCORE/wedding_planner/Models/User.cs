using System.Collections.Generic;
using wedding_planner.Models;


namespace wedding_planner.Models
{
    public class User
    {
        public int id{get;set;}
        public string firstname{get;set;}
        public string lastname{get;set;}
        public string email{get;set;}
        public string password{get;set;}
        public List<Schedule> schedules{get;set;}
        public User()
        {
            schedules = new List<Schedule>();
        }
    }
}