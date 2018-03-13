using System;

namespace basic_13
{
    class Program
    {
        static void Main(string[] args)
        {
            // Print 1-255
            Console.WriteLine("******************************");
            for(int i = 1; i <= 255; i++){
                Console.Write(i + " ");
            }
            Console.WriteLine();
            // Print odd numbers 1-255
            Console.WriteLine("******************************");
            for(int i = 1; i <= 255; i++){
                if(i%2 != 0){
                    Console.Write(i + " ");
                }
                
            }
            //Print numbers through 255 and sum
            Console.WriteLine("******************************");
            int sum = 0;
            for(int i = 1; i <= 255; i++){
                sum = sum + i;
                Console.WriteLine("New number:" + i + " Sum: "+ sum);
            }

            // Iterating through an array
            Console.WriteLine("******************************");
            int[] array = new int[]{1,3,5,7,9,13};
            int[] array2 = new int[]{-3,-5,-7};
            PrintArray(array);
            //Find Max
            Console.WriteLine("******************************");
            FindMax(array2);
            //Get Average
            Console.WriteLine("******************************");
            Average(array2);


            //Array with Odd Numbers
            Console.WriteLine("******************************");
            int[] y = new int[128];
            int x = 0;
            for(int i = 1; i<=255;i++){
                if (i%2 != 0){
                    y[x] = i;
                    x++;
                }
            }
            foreach(int n in y){
                Console.Write(n + " ");
            }
            Console.WriteLine();

            // Greater than Y
            Console.WriteLine("******************************");
            Console.WriteLine(GreaterThan(array, 4));

            // Square the values
            Console.WriteLine("******************************");
            foreach(int a in array){
            Console.WriteLine(a);
            }
            Console.WriteLine("******************************");
            int[] array3 = new int[array.Length];
            array3 = SquareValues(array);
            
            foreach(int abcdefghIAmAVaraible in array3){
            Console.WriteLine(abcdefghIAmAVaraible);
            }
            //Eliminate Negative numbers
            int[] anotherArray = new int[4]{1,5,10,-2};
            int[] resultingArray = new int[anotherArray.Length];
            resultingArray = EliminateNegatives(anotherArray);
            Console.WriteLine("******************************");
            foreach(int abcdefghIAmAVaraible in resultingArray){
                Console.WriteLine(abcdefghIAmAVaraible);
            }

            //Min Max and Average
            Console.WriteLine("******************************");
            int[] array9000 = new int[4]{1,5,10,-2};
            PrintArrayStats(array9000);


            //Shifting the Values in an Array
            int[] almostTheLastArray = new int[5]{1,5,10,7,-2};
            int[] almostTheLastResult = new int[anotherArray.Length];
            almostTheLastResult = ShiftingTheValue(almostTheLastArray);
            Console.WriteLine("******************************");
            foreach(int abcdefghIAmAVaraible in almostTheLastResult){
                Console.WriteLine(abcdefghIAmAVaraible);
            }

            //Number to String
            int[] last = new int[3]{-1,-3,2};
            object[] oopsLast = new object[anotherArray.Length];
            oopsLast = NumberToString(last);
            Console.WriteLine("******************************");
            foreach(var abcdefghIAmAVaraible in oopsLast){
                Console.WriteLine(abcdefghIAmAVaraible);
            }





        }


        public static object[] NumberToString(int[] array){
            object[] returnedArray = new object[array.Length];
            int z = 0;
            foreach(int k in array){
                if(k < 0){
                    returnedArray[z] = "Dojo";
                    z++;
                }
                else{
                    returnedArray[z] = k;
                    z++;
                }
            }
            return returnedArray;
        }



        public static void PrintArrayStats(int[] array){
            int max = array[0];
            int min = array[0];
            int total = 0;
            int average = 0;
            foreach(int a in array){
                if(a > max){
                    max = a;
                }
                if(a < min){
                    min = a;
                }
                total = total + a;
            }
            average = total/array.Length;
            Console.WriteLine("Average is " + average);
            Console.WriteLine("Min is " + min);
            Console.WriteLine("Max is " + max);
        }

        public static int[] ShiftingTheValue(int[] array){
            int[] returnedArray = new int[array.Length];
            int z = 0;
            while (z < array.Length-1){
                returnedArray[z] = array[z+1];
                z++;
            }
            returnedArray[array.Length-1] = 0;
            return returnedArray;
        }
        public static int[] EliminateNegatives(int[] array){
            int[] returnedArray = new int[array.Length];
            int z = 0;
            foreach(int k in array){
                if(k < 0){
                    returnedArray[z] = 0;
                    z++;
                }
                else{
                    returnedArray[z] = k;
                    z++;
                }
            }
            return returnedArray;
        }
        public static int[] SquareValues(int[] array){
            int[] returnedArray = new int[array.Length];
            int z = 0;
            foreach(int x in array){
                returnedArray[z]=x*x;
                z++;
            }
            return returnedArray;
        }
        public static int GreaterThan(int[] array, int y){
            int x = 0;
            foreach(int a in array){
                
                if(a > y){
                    x++;
                }
            }
            return x;
        }
        public static void PrintArray(int[] array){
            foreach(var a in array)
            Console.WriteLine(a);
        }
        public static void FindMax(int[] array){
            int max = array[0];
            foreach(int n in array){
                if (n > max){
                    max = n;
                }
            }
            Console.WriteLine("Max is " + max);
        }
        public static void Average(int[] array){
            float total = 0;
            foreach(var n in array){
                total = (float)n + total;
            }
            Console.WriteLine("Average is " + total/array.Length);
        }
    }
}
