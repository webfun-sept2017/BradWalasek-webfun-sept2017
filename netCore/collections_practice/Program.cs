using System;
using System.Collections.Generic;

namespace collections_practice
{
    class Program
    {
        static void Main(string[] args)
        {
            // First array
            int[] array1 = new int[] {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
            foreach(int a in array1){
                Console.WriteLine(a);
            }

            // Second array
            string[] array2 = new string[4];
            array2[0] = "Tim";
            array2[1] = "Martin";
            array2[2] = "Nikki";
            array2[3] = "Sara";
            foreach(string a in array2){
                Console.WriteLine(a);
            }

            // Third array
            bool[] array3 = new bool[10];
            for(int i = 0; i <10; i++){
                if ((i+2)%2 == 0){
                    array3[i] = true;
                }
                else{
                    array3[i] = false;
                }
            }
            foreach(bool a in array3){
                Console.WriteLine(a);
            }

            // Multiplication table
            int[,,] array4 = new int[10,1,10];
            for(int i = 0; i < 10; i++){
                for (int j = 0; j < 10; j++){
                    array4[i,0,j] = ((i+1)*(j+1));
                }
            }
            for(int i = 0; i < 10; i++){
                for (int j = 0; j < 10; j++){
                    Console.Write(array4[i,0,j] + " ");
                }
                Console.WriteLine();
            }
            
            // List of Flavors
            List<string> flavors = new List<string>();
            flavors.Add("Vanilla");
            flavors.Add("Chocolate");
            flavors.Add("Pistachio");
            flavors.Add("Peppermint");
            flavors.Add("Bubblegum");
            Console.WriteLine(flavors.Count);
            Console.WriteLine(flavors[2]);
            flavors.RemoveAt(2);
            Console.WriteLine(flavors.Count);

            // User Info Dictionary
            Dictionary<string,string> dict = new Dictionary<string, string>();
            dict.Add("Tim","");
            dict.Add("Martin","");
            dict.Add("Nikki","");
            dict.Add("Sara","");
            dict["Martin"]="Vanilla";
            dict["Nikki"]="Peppermint";
            dict["Sara"] = "Pistachio";
            dict["Tim"] = "Chocolate";
            foreach(var entry in dict){
                Console.WriteLine("{0}, {1}",entry.Key, entry.Value);
            }
            PrintArray(flavors);
           
            
        }


        // Attempt at making a new method
        public static void PrintArray(List<string> array){
            foreach(var a in array){
                Console.WriteLine(a);
            }
        }
    }
    
}
