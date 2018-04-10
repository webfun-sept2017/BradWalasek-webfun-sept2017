using System;
using System.Collections.Generic;
namespace wedding_planner.Models
{
    public class Wedding
    {
        public int id{get;set;}
        public string name{get;set;}
        public DateTime date{get;set;}
        public string address{get;set;}
        public List<Schedule> schedules {get;set;}
        public Wedding()
        {
            schedules = new List<Schedule>();
        }
    }
}