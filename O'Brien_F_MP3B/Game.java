import java.util.LinkedList;
import java.util.Random;

public class Game {
    private LinkedList<Player> players;
    private LinkedList<Card> pile;
    private Dealer dealer;
    private String[] patterns;

    // static methods 
    static boolean topBottom(LinkedList<Card> pile){
        if (pile.getFirst().getRank() == pile.getLast().getRank()){ 
            return true;
        } else {
            return false;
        }
    }

    static boolean doubles(LinkedList<Card> pile){
        int pileSize = pile.size();
        if (pile.size() >= 2 && pile.get(pileSize - 1).getRank() == pile.get(pileSize -2).getRank()){ 
            return true;
        } else {
            return false;
        }
    }

    static boolean sandwhich(LinkedList<Card> pile){
        int pileSize = pile.size();
        if (pile.size() >= 3 && pile.get(pileSize -1).getRank() == pile.get(pileSize -3).getRank()){
            return true;
        } else {
            return false;
        }
    }


    public LinkedList<Player> getPlayers(){
        return players;
    }

    public LinkedList<Card> getPile(){
        return pile;
    }

    public Dealer getDealer(){
        return dealer;
    }

    public String[] getPatterns(){
        return patterns;
    }

    public Game(){
        players = new LinkedList<>(); //LinkedList<Player>
        dealer = new Dealer(); //Dealer 
        pile = new LinkedList<>();//LinkedList<Card> 
        patterns = new String[3];//String 
        patterns[0] = "doubles";
        patterns[1] = "topBottom";
        patterns[2] = "sandwhich";
        LinkedList<Card> p1Hand = dealer.deals(26);
        LinkedList<Card> p2Hand = dealer.deals(26);
        Player p1 = new Player(1, p1Hand, patterns[0]);
        Player p2 = new Player(2, p2Hand, patterns[1]);
        players.add(p1);
        players.add(p2);
        
    }

    Random random = new Random();

    public Game(int s){
        int playerCount = s;
        players = new LinkedList<>();
        dealer = new Dealer();
        pile = new LinkedList<>();
        patterns = new String[3];
        patterns[0] = "doubles";
        patterns[1] = "topBottom";
        patterns[2] = "sandwhich";
        int randomNum = random.nextInt(3);
        for (int i=1; i < s+1; ++i){
            Player pi = new Player(i, dealer.deals(52 / s), patterns[randomNum]);
            players.add(pi);
        }
        for(int i = 0; i < 52 % s; ++i){
            Card e = dealer.deal();
            pile.add(e);
        };
    }

    private Player nextPlayer(Player currentPlayer){
        int playerCount = players.size();
        int index = players.indexOf(currentPlayer);
        Player nextPlayer;
        if (currentPlayer == null){
            nextPlayer = players.get(0);
        } else if (index + 1 == playerCount){
            nextPlayer = players.get(0);
        } else{
            nextPlayer = players.get(index +1);
        }
        return nextPlayer;

    }

    public int getLargestHand(){
        int largestHand = 0;
       int handCount;
       for(Player P: players){
       handCount = P.getHandSize();
        if(handCount > largestHand){
            largestHand = handCount;
        }
    }
    return largestHand;
}

public int getLargestPlayer(){
    int playerIndex = 0;
    for(Player p: players){
        if(p.getHandSize() == 52){
            playerIndex = p.getPlayerNum();
            break;
        }
    }
    return playerIndex;
}

//if(topBottom == true){
    // for(Player p: players){
       // if (p.getPattern() == 'topBottom'){
//          p.addPile();
//          break;
       //}
   // }
   //p.playCard();
//}

    public int play(){
       Player nextPlayer; 
       Player lastPlayer = null;

        int largestHandCount = getLargestHand(); //size of the largest hand, will be 52 if a player has all cards 
        int largestPlayerIndex = getLargestPlayer();

        LinkedList<Player> playersToRemove = new LinkedList<>(); // allows for players to be removed from the list after iterating over the whole list

        boolean shouldBreak = false; // will break out of the main while loop

       while( largestHandCount < 52){ //while no player has all cards
        if(players.size() == 1){ // if there is only one player left
        players.get(0).addPile(pile);//get the index of the last remaining player, and add the pile to the players hand 
        break;}
        Player p1 = players.get(0); //initial player is always player 1
        Card c = p1.playCard(); //player one starting off the game with 1 card
        pile.add(c); // adding that card to the pile
        lastPlayer = p1; 
        if (shouldBreak) break;
        System.out.print(pile);
        if(pile.getLast() == null){
            pile.removeLast();
        }
       while(pile.getLast().getRank() != 11 && pile.getLast().getRank() != 12 && pile.getLast().getRank() != 13 && pile.getLast().getRank() != 14 ){ // while the last card played is not a face card or ace
       for(Player p: players){ // i learned that you cannot edit a linkedlist while iterating over it from chat gpt, which taught me how to create my method of taking players out of the list.
        if (p.getHandSize() ==0){ //check to see if any players have empty hands, and if they do, remove them
            playersToRemove.add(p);
        }
       }
       if (shouldBreak) break;
       System.out.println("players To Remove " + playersToRemove);
       players.removeAll(playersToRemove); // removing players with empty hand 
       System.out.println("players Left " + players.size());
       if(players.size() == 1){ // if there is only one player left, add the pile to their hand, and break the game out of the loop
        players.get(0).addPile(pile);
        shouldBreak = true;

        break;
       }

       if (shouldBreak) break;
        nextPlayer = nextPlayer(lastPlayer); //set the next player as the player 1 index higher than the last player
        Card C = nextPlayer.playCard(); 
        pile.add(C);
        lastPlayer = nextPlayer; // update who the last player was 
               if (shouldBreak) break;
        if(pile.getLast() == null){
            pile.removeLast();
        }
        if(pile.getFirst() == null){
            pile.remove(0);
        }
        if(topBottom(pile) == true){
            LinkedList<Player> playersWithThisPattern = new LinkedList<>();
            for (Player p: players){
                if (p.getPattern() == "topBottom"){
                    playersWithThisPattern.add(p);
                }
                int amountOfPlayersWithPattern = playersWithThisPattern.size();
                if(amountOfPlayersWithPattern == 0){
                    break;
                }
                int randomNum = random.nextInt(amountOfPlayersWithPattern);
                Player e = players.get(randomNum);
                e.addPile(pile);
                Card z = e.playCard();
                pile.add(z);
                System.out.println(e + "Just slapped on top bottom ");
                playersWithThisPattern.clear();
                break;
            }
        }
               if (shouldBreak) break;

        if(doubles(pile) == true){
            LinkedList<Player> playersWithThisPattern = new LinkedList<>();
            for (Player p: players){
                if (p.getPattern() == "doubles"){
                    playersWithThisPattern.add(p);
                }
                int amountOfPlayersWithPattern = playersWithThisPattern.size();
                if (amountOfPlayersWithPattern == 0){
                    break;
                }
                int randomNum = random.nextInt(amountOfPlayersWithPattern);
                Player e = players.get(randomNum);
                e.addPile(pile);
                Card z = e.playCard();
                pile.add(z);
                System.out.println(e + "Just slapped on doubles ");
                playersWithThisPattern.clear();
                break;
            }
        }
               if (shouldBreak) break;

         if(sandwhich(pile) == true){
            LinkedList<Player> playersWithThisPattern = new LinkedList<>();
            for (Player p: players){
                if (p.getPattern() == "sandwhich"){
                    playersWithThisPattern.add(p);
                }
                int amountOfPlayersWithPattern = playersWithThisPattern.size();
                if(amountOfPlayersWithPattern ==0){
                    break;
                }
                int randomNum = random.nextInt(amountOfPlayersWithPattern);
                Player e = players.get(randomNum);
                e.addPile(pile);
                Card z = e.playCard();
                pile.add(z);
                System.out.println(e + "Just slapped on sandwhich ");
                playersWithThisPattern.clear();
                break;
            }
        }
               if (shouldBreak) break;

        //if(topBottom == true){
    // for(Player p: players){
       // if (p.getPattern() == 'topBottom'){
//          p.addPile();
//          break;
       //}
   // }
   //p.playCard();
//}

        if(players.size() == 1){ //again, check if there is only one player left
        players.get(0).addPile(pile);
        shouldBreak = true;
        break;
       }
    //    if (shouldBreak) break;
       } 
       if (shouldBreak) break; // KEEP THIS ONE 
       if(pile.getLast().getRank() == 11){ // if the last card played is a jack 
        if (shouldBreak) break;
            nextPlayer = nextPlayer(lastPlayer); //set the next player, and have them play a card
            Card C = nextPlayer.playCard();
            pile.add(C);
                    if (shouldBreak) break;
                    System.out.println(pile);
                    if(pile.getLast() == null){
            pile.removeLast();
        }
                if (pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){ // if they now play a face card, continue the game. 
                lastPlayer = nextPlayer; // update who the last player was 
        } else{ // if the player that is up does not play a face card
                int index = players.indexOf(lastPlayer);
                players.get(index).addPile(pile); // add the pile to the player who played the original face card
                Card g = lastPlayer.playCard(); // now have that player play another card, starting the game back up.
                pile.add(g);

            }
        } else if(pile.getLast().getRank() == 12){ // if the last card played was a queen 
            nextPlayer = nextPlayer(lastPlayer); // have the next player play a card and add it to pile
            Card C = nextPlayer.playCard();
            pile.add(C);
            if (shouldBreak) break;
            System.out.println(pile);
            if(pile.getLast() == null){
            pile.removeLast();
        }
                if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){ //if they play a face card
                lastPlayer = nextPlayer; //continue game, since a face card was played 
                } else{
                    if(nextPlayer.getHandSize()==0){ // if the player just played their last card, remove that player. 
                        players.remove(nextPlayer);
                        int index = players.indexOf(lastPlayer);
                    players.get(index).addPile(pile); // add the pile to the winning players hand 
                    Card g = lastPlayer.playCard();
                    pile.add(g); // have that player play a card, and start the game back up
                    }
                    else{ // the player gets one more chance to play a face card
                        Card G = nextPlayer.playCard();
                        pile.add(G);
                            if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){
                            lastPlayer = nextPlayer; // if they now play a face card, continue the game
                } else{ // if they dindt play a face card, add the pile to the hand of the player who played the original queen 
                    int index = players.indexOf(lastPlayer);
                    players.get(index).addPile(pile);
                    Card g = lastPlayer.playCard();
                    pile.add(g);
                    
                }
                     } }
        } else if(pile.getLast().getRank() == 13){ // if a king was played
            nextPlayer = nextPlayer(lastPlayer);
            Card C = nextPlayer.playCard();
            pile.add(C);
                   if (shouldBreak) break;
                   System.out.println(pile);
                   if(pile.getLast() == null){
            pile.removeLast();
        }
                if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){
                    lastPlayer = nextPlayer;
                } else{
                    if(nextPlayer.getHandSize()==0){ // if they played their last card
                        players.remove(nextPlayer); // remove that player, and continue the game
                        int index = players.indexOf(lastPlayer);
                    players.get(index).addPile(pile);
                    Card g = lastPlayer.playCard();
                    pile.add(g);
                    System.out.println("LOOK: 210");
                    }else{
                    Card G = nextPlayer.playCard(); //the player's second chance to draw a face card 
                    pile.add(G); 
                    if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){
                        lastPlayer = nextPlayer; // if they get a face card, continue the game 
                    } else{
                        if(nextPlayer.getHandSize()==0){ // if they didnt draw a face card and that was their last card, add pile and continue 
                        players.remove(nextPlayer);
                        int index = players.indexOf(lastPlayer);
                    players.get(index).addPile(pile);
                    Card g = lastPlayer.playCard();
                    pile.add(g);
                    }else{ // now the players third try to get a face card 
                        Card E = nextPlayer.playCard();
                        pile.add(E);
                        if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){
                            lastPlayer = nextPlayer; // if they get a face card, continue play 
                        } else{
                            int index = players.indexOf(lastPlayer);
                            players.get(index).addPile(pile);
                            Card g = lastPlayer.playCard();
                            pile.add(g);
                          }  }
                    }


                }}
        } else if(pile.getLast().getRank() == 14){
            nextPlayer = nextPlayer(lastPlayer);
            Card C = nextPlayer.playCard();
            pile.add(C);
                   if (shouldBreak) break;
                System.out.println(pile);
                if(pile.getLast() == null){
            pile.removeLast();
        }
                if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){
                    lastPlayer = nextPlayer;
                } else{
                    if(nextPlayer.getHandSize()==0){
                        players.remove(nextPlayer);
                        int index = players.indexOf(lastPlayer);
                    players.get(index).addPile(pile);
                    Card g = lastPlayer.playCard();
                    pile.add(g);
                    }else{
                    Card G = nextPlayer.playCard();
                    pile.add(G);
                    if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){
                        lastPlayer = nextPlayer;
                    } else{
                        if(nextPlayer.getHandSize()==0){
                        players.remove(nextPlayer);
                        int index = players.indexOf(lastPlayer);
                    players.get(index).addPile(pile);
                    Card g = lastPlayer.playCard();
                    pile.add(g);
                    }else {
                        Card E = nextPlayer.playCard();
                        pile.add(E);
                        if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){
                            lastPlayer = nextPlayer;
                        } else{
                            if(nextPlayer.getHandSize()==0){
                        players.remove(nextPlayer);
                        int index = players.indexOf(lastPlayer);
                    players.get(index).addPile(pile);
                    Card g = lastPlayer.playCard();
                    pile.add(g);
                    }else{
                            Card F = nextPlayer.playCard();
                            pile.add(F);
                            if(pile.getLast().getRank() == 11 || pile.getLast().getRank() == 12 || pile.getLast().getRank() == 13 || pile.getLast().getRank() == 14){
                                lastPlayer = nextPlayer;
                            }else{
                                int index = players.indexOf(lastPlayer);
                            players.get(index).addPile(pile);}
                            Card g = lastPlayer.playCard();
                            pile.add(g);
                        }}
                     } }


                  }  }}
       System.out.println("52 cards thing");
       for (Player p: players){
        System.out.println(p);
       }
       System.out.println("PILE");
        System.out.println(pile);
        
    }
    System.out.println();
    System.out.println();
    System.out.println();
    System.out.println("WINNER IS PLAYER NUMBER: " + players.getFirst());
return largestPlayerIndex;}
    

    public String toString(){
        String s = "";
        s+= "Players: " + players.toString() + "\n";
        return s;

    }





    }



    

