
import java.util.LinkedList;
public class Dealer { //dealer class
    
    private Deck m_deck;
 // member variable 
    public Dealer(){
        m_deck = new Deck();
    }

    public LinkedList<Card> deals(int n){
        LinkedList<Card> dealtCards = new LinkedList<>();
        if (m_deck.size() == 0 || m_deck.size() < n){
            return dealtCards;
        }else 
            {for(int i = 0; i < n; ++i ){
            dealtCards.add(m_deck.deal());}
        }
        return dealtCards;
    }

    public Card deal(){
        Card C = m_deck.deal();
        return C;
    }


    public Card getCard(){
        if(m_deck.size() == 0){
            return null;
        }else{
            Card C = m_deck.deal();
            return C;
        }}
    

    public int size(){
        int cardsInDeck = 0;
        cardsInDeck = m_deck.size();
        return cardsInDeck;
    }

    public String toString(){
        return m_deck.toString();
    }
}
