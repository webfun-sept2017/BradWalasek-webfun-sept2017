using System;
using System.Collections.Generic;

namespace boxing_unboxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> x = new List<object>();
            x.Add(7);
            x.Add(28);
            x.Add(-1);
            x.Add(true);
            x.Add("chair");
            int sum = 0;
            foreach(var a in x){
                Console.WriteLine(a);
                if (a is int){
                    sum = sum + (int)a ;
                }
            }
        Console.WriteLine("Sum is " + sum);
        }
    }
}
