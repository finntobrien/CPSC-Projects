/**
 * @author Finbar O'Brien
 * @version 1.1
 * A class to create object representations of an order of latte objects 
 * 
 */


public class LatteOrder{ // define latteOrder class
    private Latte[] m_order; // set latte array member variable
    private int m_numLattes; //member variable checking how ma ny lattes are in an order
    /** a variable to help with adding lattes to the array. This tracks how many have been added so far */
    private static int addedLatteCount = 0; 

    public LatteOrder(){ /** // default constructor  */
        m_numLattes = 1;
        m_order = new Latte[m_numLattes];
        m_order[0] = new Latte();
    }

    /** @param numLattes */
    public LatteOrder(int numLattes){ // finds how many lattes are in the order.
        m_numLattes = numLattes; // sets num lattes member variable 
        m_order = new Latte[m_numLattes];
    }

    /**@param latte */
    /** adds latte objects to the array */
    public int addLatte(Latte latte){ // adds lattes to the array 
        if (m_numLattes > addedLatteCount ){  // checks if there is space to add another latte to the array 
            m_order[addedLatteCount] = latte; // puts latte at the index of the amount of added lattes so far, into the array 
            ++ addedLatteCount; // increments the amount of lattes added so far 
            return 1;
        } else{
            return -1; // returns -1 if there is no space to add another latte 
        }
    }

    /** calculates total cost of the array  */
    /** @return totalCost */
    public double calcTotal(){ // calculates cost of an array of lattes 
        double totalCost = 0;
        double c = 0;
        for (int i = 0; i < m_numLattes; ++i){
            c = m_order[i].calcCost(); // calls upon the calcCost method in Latte class 
            totalCost += c; // increments total cost 
        }
        return totalCost;
    }
/** ToString method */
    public String toString(){ // prints out required information associated with the latte order 
        String s = "Order: " + "\n"; 
        s+= "Total Cost: " + calcTotal() + "\n";
        for (int i = 0; i < m_numLattes; ++i){
            s+= "Latte " + (i) + "\n";
            s+= m_order[i].toString() + "\n";
        }
        return s;
    }



}