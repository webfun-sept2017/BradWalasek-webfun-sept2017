using System;
using System.Collections.Generic;
namespace cards{
    public class Card{
        public string stringVal;
        public string suit;
        public int value;
        public Card(string strval, string su, int numval){
            stringVal = strval;
            suit = su;
            value = numval;
        }
    }
    public class Deck{
        public List<Card> DeckofCards = new List<Card>();
        public Deck(){
            string[] suits = new string[]{"Hearts", "Diamonds", "Clubs", "Spades"};
            foreach(string suit in suits){
                for(int i = 1; i < 14; i++){
                    if(i == 1){
                        DeckofCards.Add(new Card("Ace", suit, i));
                    }
                    else if(i>1 && i < 11){
                        DeckofCards.Add(new Card(i.ToString(), suit, i));
                    }
                    else if (i == 11){
                        DeckofCards.Add(new Card("Jack", suit, i));
                    }
                    else if (i == 12){
                        DeckofCards.Add(new Card("Queen", suit, i));
                    }
                    else{
                        DeckofCards.Add(new Card("King", suit, i));
                    }
                }
            }
        }
        public Card Deal(){
            Card dealt = DeckofCards[0];
            Console.WriteLine(dealt.stringVal +" "+ dealt.suit);
            DeckofCards.RemoveAt(0);
            return dealt;
        }
        public void Shuffle(){
            Random rand = new Random();
            for(int i = 0; i < 2000; i++){
                int location = rand.Next(0,52);
                Card moved = DeckofCards[location];
                DeckofCards.RemoveAt(location);
                DeckofCards.Insert(rand.Next(0,52), moved);
            }
        }
        public void Reset(){
            DeckofCards.Clear();
            string[] suits = new string[]{"Hearts", "Diamonds", "Clubs", "Spades"};
            foreach(string suit in suits){
                for(int i = 1; i < 14; i++){
                    if(i == 1){
                        DeckofCards.Add(new Card("Ace", suit, i));
                    }
                    else if(i>1 && i < 11){
                        DeckofCards.Add(new Card(i.ToString(), suit, i));
                    }
                    else if (i == 11){
                        DeckofCards.Add(new Card("Jack", suit, i));
                    }
                    else if (i == 12){
                        DeckofCards.Add(new Card("Queen", suit, i));
                    }
                    else{
                        DeckofCards.Add(new Card("King", suit, i));
                    }
                }
            }
        }

        

    }
    public class Player{
        string playerName;
        List<Card> hand = new List<Card>();
        public Player(string name = "Anonymous"){
            playerName = name;
        }
        public void draw(Deck deck){
            hand.Add(deck.Deal());
        }
        public Card discard(int i){
            if(hand[i-1] is Card){
                Card returned = hand[i-1];
                hand.RemoveAt(i-1);
                return returned;
            }
            else{
                return null;
            }
        }
        public void check(){
            foreach(Card x in hand){
                Console.WriteLine(x.stringVal + " " + x.suit);
            }
        }

    }
}