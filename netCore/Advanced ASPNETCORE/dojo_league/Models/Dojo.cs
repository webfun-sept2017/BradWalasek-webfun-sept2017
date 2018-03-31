using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace dojo_league.Models
{
    public class Dojo : BaseEntity
    {
        public Dojo(){
            clan = new List<Ninja>();
        }
        public string name{get;set;}
        public string location{get;set;}
        public string description{get;set;}
        public int id;
        public ICollection<Ninja> clan{get;set;}
    }
}