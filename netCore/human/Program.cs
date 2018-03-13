using System;

namespace human
{
    class Program
    {
        static void Main(string[] args)
        {
            Human brad = new Human("Brad",10,10,10,1000);
            Human mitch = new Human("Mitch", 8,10,10,1000);
            Console.WriteLine(mitch.health);
            brad.attack(mitch);
            Console.WriteLine(mitch.health);
            brad.attack(mitch);
            Console.WriteLine(mitch.health);
            Console.WriteLine(brad.health);
            mitch.attack(brad);
            Console.WriteLine(brad.health);
        }
    }
    public class Human{
        public string name;
        public int strength = 3;
        public int intelligence= 3;
        public int dexterity = 3;
        public int health = 100;
        public Human(string var = "nobody"){
            name = var;
        }
        public Human(string var = "nobody", int str = 3, int dex = 3, int intel = 3, int hea = 100){
            name = var;
            strength = str;
            intelligence = intel;
            dexterity = dex;
            health = hea;
        }
        public void attack(object attacked){
            int damage = 5*strength;
            if(attacked is Human){
                
                Console.WriteLine("Human!");
                Human hurt = (Human)attacked;
                hurt.health = hurt.health - damage;
                attacked = (object)hurt;
            }
        }

    }
}
