using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?

            //Who is the youngest artist in our collection of artists?

            //Display all artists with 'William' somewhere in their real name

            //Display the 3 oldest artist from Atlanta

            //(Optional) Display the Group Name of all groups that have members that are not from New York City
            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan
            
            
            
            // First Task
            var vernonite = from people in Artists
                            where people.Hometown == "Mount Vernon"
                            select new {people.RealName, people.Hometown, people.Age};
                            var guy = vernonite.First();
            Console.WriteLine(guy.RealName + " " + guy.Age);

            // Second Task
            var listByAge = from people in Artists
                            orderby people.Age ascending
                            select new {people.RealName, people.Age};
            var youngest = listByAge.First();
            Console.WriteLine(youngest.RealName + " " + youngest.Age);

            // Third Task
            var findingWilliam = from people in Artists
                                 where people.RealName.Contains("William") 
                                 select new {people.RealName};
            foreach(var x in findingWilliam){
                Console.WriteLine(x.RealName);
            }

            // Fourth Task
            var shortnames = from item in Groups
                                     where item.GroupName.Length < 8
                                     select new {item.GroupName};
            foreach(var x in shortnames){
                Console.WriteLine(x.GroupName);
            }
            var oldestInAtlanta = from people in Artists
                            where people.Hometown == "Atlanta"
                            orderby people.Age descending
                            select new {people.RealName, people.Age};
            var topThree = oldestInAtlanta.Take(3);
            foreach(var x in topThree){
                Console.WriteLine(x.RealName);
            }

            

        }
    }
}
