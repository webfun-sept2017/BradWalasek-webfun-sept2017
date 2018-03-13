using System;
using System.Collections.Generic;

namespace cards
{
    class Program
    {
        static void Main(string[] args)
        {
            Deck deck1 = new Deck();
            Player Brad = new Player("Brad");
            Brad.draw(deck1);
            Brad.draw(deck1);
            Brad.draw(deck1);
            Brad.draw(deck1);
            Brad.draw(deck1);
            Brad.check();
            Brad.discard(1);
            Brad.check();
        }
    }
    
}
