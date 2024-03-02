import java.util.LinkedList;


public class TestCards {
    public static void main(String[] args){

    Card AoS = new Card();


    Card card1 = new Card(3,2);


   // Dealer deal1 = new Dealer();
    //Player p1 = new Player(1, deal1.deals(8), "abc");
    //System.out.println(p1);
    //System.out.println(p1.playCard());
    //System.out.println(p1);
    //Game g1 = new Game();
    //System.out.println(g1);
   //g1.play();
    //System.out.println(g1);
    //Game g2 = new Game(4);
    //System.out.println(g2);
    //LinkedList<Card> pile1 = new LinkedList<>();
    //Dealer deal2 = new Dealer();
    //Player p3 = new Player(3, deal2.deals(8), "top-bottom");
    //System.out.println(p3);
    //pile1 = deal2.deals(5);
    //p3.addPile(pile1);
    //System.out.println(p3);

    Game g4 = new Game(7);
    g4.play();
    
    }
}
