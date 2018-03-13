using System;
using System.Collections.Generic;
using System.Linq;

namespace console
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            List<object> newList = new List<object>()
            {
                "Brad",
                "Kate",
                "Danica",
                "Stella",
                "Kellan"
            };
            foreach(string item in newList){
                Console.WriteLine(item);
            }
            
            Console.WriteLine("************");
            
            // Product[] products = {
            //     new Product { Name = "Jeans", Category = "Clothing", Price = 24.7 },
            //     new Product { Name = "Socks", Category = "Clothing", Price = 8.12 },
            //     new Product { Name = "Scooter", Category = "Vehicle", Price = 99.99 },
            //     new Product { Name = "Skateboard", Category = "Vehicle", Price = 24.99 },
            // };
            // foreach(Product item in products){
            //     Console.WriteLine($"{item.Name} {item.Price}");
            // }

            // var foundProducts = from match in products
            //         orderby match.Price descending
            //         select new { match.Name, match.Price };

            // foreach(var item in foundProducts){
            //     Console.WriteLine($"{item.Name} {item.Price}");
            // }
            
            // Person[] family = new Person[]{
            //     new Person {Name = "Kate", Age = 30, Gender = 'F'},
            //     new Person {Name = "Brad", Age = 26, Gender = 'M'},
            //     new Person {Name = "Danica", Age = 5, Gender = 'F'},
            //     new Person {Name = "Stella", Age = 5, Gender = 'F'},
            //     new Person {Name = "Kellan", Age = 0, Gender = 'M'},
            // };
            // var searched = from match in family
            //                 orderby match.Name ascending
            //                 select new {match.Name, match.Age};


            // foreach(var item in searched){
            //     Console.WriteLine($"{item.Name} {item.Age}");
            // }

            Person[] family = new Person[]{
                new Person {Name = "Kate", Age = 30, Gender = 'F'},
                new Person {Name = "Brad", Age = 26, Gender = 'M'},
                new Person {Name = "Danica", Age = 5, Gender = 'F'},
                new Person {Name = "Stella", Age = 5, Gender = 'F'},
                new Person {Name = "Kellan", Age = 0, Gender = 'M'},
            };
            var TransformedList = family.Where(Person=>Person.Age > 1);


            foreach(var item in TransformedList){
                Console.WriteLine($"{item.Name} {item.Age}");
            }


        }
    }
}
