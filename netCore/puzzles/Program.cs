using System;

namespace puzzles
{
    class Program
    {
           public static int[] RandomArray(){
            Random rand = new Random();
            int[] array = new int[10];
            for(int i = 0; i<10; i++){
                array[i] = rand.Next(1,25);
            }
            int max = array[0];
            int min = array[0];
            int total = 0;
            foreach(int x in array){
                if(x > max){
                    max = x;
                }
                if(x < min){
                    min = x;
                }
                total = total + x;
            }
        Console.WriteLine("Max: " + max + " Min: " + min);
        Console.WriteLine("Total is " + total);
        return array;
        }

        public static string TossCoin(Random rand){
            Console.WriteLine("Tossing a Coin!");
            // Random rand = new Random();
            string result;
            int x = rand.Next(1,3);
            if(x == 1){
                Console.WriteLine("Heads");
                result = "Heads";
            }
            else{
                Console.WriteLine("Tails");
                result = "Tails";
            }
            return result;
        }
        public static double TossMultipleCoins(double x, Random rand){
            double headcount = 0;
            string cointoss;
            for(int i = 0; i < x; i++){
                cointoss = TossCoin(rand);
                if(cointoss == "Heads"){
                    headcount++;
                }
            }
            
            double result = headcount/x;
            return result;
        }
        public static string[] Names(string[] names){
            Random rand = new Random();
            int counter = 0;
            int l = names.Length;
            int location;
            int location2;
            string swap;
            
            for(int i = 0; i < 100; i++){
                location = rand.Next(0,l);
                location2 = rand.Next(0,l);
                swap = names[location];
                names[location] = names[location2];
                names[location2] = swap;            
            }
            foreach(string x in names){
                Console.WriteLine(x);
                if (x.Length > 5){
                    counter++;
                }
                
            }
            string[] returned = new string[counter];
            counter = 0;
            foreach(string x in names){
                if (x.Length > 5){
                    returned[counter] = x;
                    counter++;
                }
            }
            return returned;
        }
        static void Main(string[] args)
        {
            Random rand = new Random();
            
            // string a = TossCoin(rand);
            // double b = TossMultipleCoins(5, rand);
            // Console.WriteLine(b);
            string[] list = new string[5]{"Todd","Tiffany","Charlie", "Geneva", "Sydney"};
            string[] newList = Names(list);
            Console.WriteLine("**********************");
            foreach(string x in newList){
                Console.WriteLine(x);
            }
        }
    }
}
