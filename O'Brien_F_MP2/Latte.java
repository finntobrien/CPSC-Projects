/**
 * A class to create object representations of a Latte 
 * @author Finbar O'Brien
 * @version 1.1
 * @see LatteOrder
 */

public class Latte { // define Latte class 
    // member variables
    /** size of the latte  */
    private String m_size;  
    /** number of pumpkin sauce pumps */
    private int m_pumps;
    /** type of milk */
    private String m_milk;
    /** number of shots of espresso */
    private int m_shots;
    /** true or false to if there is whipped cream in the latte  */
    private boolean m_cream;

    public Latte(){ //default constructor 

        m_size = "grande";
        m_pumps = 4;
        m_milk = "2%";
        m_shots = 2;
        m_cream = true;
    }
/**@param size */
/** @param pumps */
/** @param milk */
/** @param shots */
/** @param cream */
    public Latte(String size, int pumps, String milk, int shots, boolean cream){ // fully paramterized latte constructor 
        m_size = size;
        m_pumps = pumps;
        m_milk = milk;
        m_shots = shots;
        m_cream = cream;

    }
/** copy constructor */
    public Latte(Latte latteToCopy){ // copy constructor 
        this.m_size = latteToCopy.m_size;
        this.m_pumps = latteToCopy.m_pumps;
        this.m_milk = latteToCopy.m_milk;
        this.m_shots = latteToCopy.m_shots;
        this.m_cream = latteToCopy.m_cream;
    }
/** @return m_size */
    public String getSize(){ // accessor of size 
        return m_size;
    }
/** @return m_pumps */
    public int getPumps(){ // accessor of pumps
        return m_pumps;
    }
/** @return m_milk */
    public String getMilk(){ // accessor of milk
        return m_milk;
    }
/** @return m_shots */
    public int getShots(){ // accessor of shots 
        return m_shots;
    }
/** @return m_cream */
    public boolean getCream(){ // accessor of cream
        return m_cream;
    }
    
    public void setSize(String newSize){ // modifier of size
        m_size = newSize;
    }

    public void setPumps(int newPumps){ // modifier of  pumps
        m_pumps = newPumps;
    }

    public void setMilk(String newMilk){ // modifier of milk
        m_milk = newMilk;
    }

    public void setShots(int newShots){ // modifier of shots
        m_shots = newShots;
    }

    public void setCream(boolean newCream){ // modifier of cream
        m_cream = newCream;
    }
/** calculates cost of a latte */
    public double calcCost(){ 
        double cost = 0; // sets intitial values to zero, because these will be replaced 
        double sizeCost = 0;
        double pumpsCost = 0;
        double milkCost = 0;
        double shotsCost = 0;
        double creamCost = 0;

        if ( m_size == "Tall" || m_size == "tall"){ // checks latte size and associates price 
            sizeCost = 2;
        } else if (m_size == "Grande" || m_size == "grande"){
            sizeCost = 2.5;
        } else {
            sizeCost = 3;
        }

        pumpsCost = 0.25 * m_pumps; //calculates pump cost 

        if (m_milk == "2%" || m_milk == "whole" || m_milk == "Whole"){ //checks milk type and associates cost 
            milkCost = 0;
        } else{
            milkCost = .75;
        }

        shotsCost = 1 * m_shots; //calculates shots cost 

        if (m_cream == true){
            creamCost = 0.5;
        } else{
            creamCost = 0.0;
        }

        cost = sizeCost + pumpsCost + milkCost + shotsCost + creamCost; // calculates total cost of the latte 
        return cost;
    }

    /** to string method */
    public String toString(){ // prints out info associated with the latte 
        String s ="";
        s+= "   Cost:" + calcCost() + "\n";
        s+= "   Size: " + m_size + "\n";
        s+= "   Pumpkin Sauce Pumps: " + m_pumps + "\n";
        s+= "   Milk Type: " + m_milk + "\n";
        s+= "   Espresso Shots: " + m_shots + "\n";
        s+= "   Whipped Cream: " + m_cream + "\n";
        return s;
        }

        /** equals method */
    public boolean equals (Object l){ // checks if two lattes are equal to each other 
        if (this == l){
            return true;
        }
        if (! (l instanceof Latte)){
            return false;
        }
        Latte s = (Latte) l;
        
        return ((this.m_size.equals(s.m_size) && (this.m_pumps == s.m_pumps) && (this.m_milk.equals(s.m_milk) && (this.m_shots == s.m_shots) && (this.m_cream == s.m_cream))));

    }

    

}