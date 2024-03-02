

import java.util.LinkedList;
import java.util.Random;

public class Deck {
    private LinkedList<Card> m_cards;

    public Deck(){
        m_cards = new LinkedList<Card>();
        for (int i=2; i<15; ++i){
            for (int j=0; j<4; ++j){
                Card c = new Card(i,j);
                m_cards.add(c);
            }
        }
    }

    public Deck(Deck cardsToCopy){
        m_cards = new LinkedList<Card>();

        for (Card c1 : cardsToCopy.m_cards){
            Card newC1 = new Card(c1);
            m_cards.add(newC1);
        }
    }

    public String toString(){
        String s = "";
        for(Card c : m_cards){
            s+= c.toString();
        }
        return s;
    }

    public int size(){
        int cardCount = 0;
        for(Card c : m_cards){
            cardCount += 1;
        }
        return cardCount;
    }

    public Card getCard(){
        if (m_cards.size() == 0){
            return null;
        }
        else{
            Card C = m_cards.get(0);
            return C;
        }
    }

    Random random = new Random();

    public Card deal(){
        if (m_cards.size() == 0){
           return null; // i got this line from troubleshooting on the internet
        }
        int min = 0;
        int max = m_cards.size();
        int randomInt = random.nextInt(m_cards.size()); // got this from the internet in combination with the notion notes. max - min +1
    
        return m_cards.remove(randomInt);
    }
}
