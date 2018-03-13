using System;
using DbConnection;

namespace CRUD
{
    class Program
    {
        static void Main(string[] args)
        {
            Read();
            Insert();
        }
        public static void Read(){
            var a = DbConnector.Query("SELECT * FROM USERS");
            foreach(var x in a){
                Console.WriteLine(x["FirstName"]);
            }
        }
        public static void Insert(){
            Console.WriteLine("First Name");
            string first = Console.ReadLine();
            Console.WriteLine("Last Name");
            string last = Console.ReadLine();
            Console.WriteLine("Favorite number");
            int fav = Int32.Parse(Console.ReadLine());
            Console.WriteLine("Purpose");
            string purpose = Console.ReadLine();
            Console.WriteLine("Job");
            string job = Console.ReadLine();
            Console.WriteLine("Hobby");
            string hobby = Console.ReadLine();
            DbConnector.Execute("INSERT into `consoledb`.`Users` (`FirstName`, `LastName`, `FavoriteNumber`, `Purpose`, `Job`, `Hobby`) VALUES('"+first+"','"+last+"','"+fav+"','"+purpose+"','"+job+"','"+hobby+"')");
            Read();
        }
    } 
}
