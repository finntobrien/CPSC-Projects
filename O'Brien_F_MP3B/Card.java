// card class
public class Card {
    private int m_rank;
    private int m_suit;
    private int[] m_card;
    //member/static variables

    public static final int HEARTS = 0;
    public static final int SPADES = 1;
    public static final int CLUBS = 2;
    public static final int DIAMONDS = 3;

    public static final int JACK = 11;
    public static final int QUEEN = 12;
    public static final int KING = 13;
    public static final int ACE = 14;   

    public Card(){ // default constructor, 1 by 2 array card
        m_card = new int[2];
        m_rank = ACE;
        m_suit = SPADES;
        m_card[0] = m_rank;
        m_card[1] = m_suit;
    }

    public Card(int r, int s){ //overloaded constuctor
        m_card = new int [2];
        m_rank = r;
        m_suit = s;
        m_card[0] = m_rank;
        m_card[1] = m_suit;
    }

    public Card (Card cardToCopy){ //copy constructor
        this.m_rank = cardToCopy.m_rank;
        this.m_suit = cardToCopy.m_suit;

    }
// basic methods

    public int getRank(){
        return m_rank;
    }

    public int getSuit(){
        return m_suit;
    }

    public void setRank(int newRank){
        m_rank = newRank;
    }

    public void setSuit(int newSuit){
        m_suit = newSuit;
    }



    public String toString(){ //tostring 
        String s = "";
        String suitName = "";
        String rank = "";

        if (m_suit == 0){ //checking suit name to print out
            suitName = "HEARTS";
        } else if (m_suit == 1){
            suitName = "SPADES";
        } else if (m_suit == 2){
            suitName = "CLUBS";
        } else {
            suitName = "DIAMONDS";
        }

        if(m_rank < 11){
            s += m_rank + " of " + suitName + "\n"; // making sure face cards print as their faces, not a number value
        } else if (m_rank == 11){
            s += "JACK" + " of " + suitName + "\n";
        } else if (m_rank ==12){
            s += "QUEEN" + " of " + suitName + "\n";
        } else if (m_rank == 13){
            s += "KING" + " of " + suitName + "\n";
        } else if (m_rank == 14){
            s += "ACE" + " of " + suitName + "\n";
        }

        return s;

    }
}
