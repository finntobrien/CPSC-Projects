import java.util.LinkedList;


public class Player {
    //member variables

    private int playerNum;
    private LinkedList<Card> hand;
    private String pattern;


    public Player(int playerNumber, LinkedList<Card> playerHand, String playerPattern){
        playerNum = playerNumber;
        hand = playerHand;
        pattern = playerPattern;
    }

    public Card playCard(){
        if(!hand.isEmpty()){ //i found out I must include this line from the internet when troubleshooting an outofbounds error
        return hand.remove(0);}
        else{
            return null;
        }

    }

    public int getHandSize(){
        int handSize = 0;
        for (Card c: hand){
            handSize += 1;
        }
        return handSize;
    }

    public LinkedList<Card> addPile(LinkedList<Card> pile){
        for (Card C : pile){
            hand.add(C);
        }
        pile.clear();
        return hand;
    }

    public int getPlayerNum(){
        return playerNum;
    }

    public LinkedList<Card> getHand(){
        return hand;
    }


    public String getPattern(){
        return pattern;
    }

    public String toString(){
        String s = "";
        s+= "Player Number: " + playerNum + "\n";
        s+= "Player Pattern: " + pattern + "\n";
        // s+= "Player Hand: " + hand + "\n"; 
        s+= "Player Hand Size:  " + hand.size() + "\n";
        
        return s;
    }
        
    
    
}
