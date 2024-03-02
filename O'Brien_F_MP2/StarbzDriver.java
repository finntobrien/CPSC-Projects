public class StarbzDriver{

    public static void main(String[] args){
        Latte tallPSL = new Latte("tall",3,"almond",3,true);
        Latte ventiPSL = new Latte("venti",5,"whole",4,false);
        Latte ventiPSL2 = new Latte(ventiPSL);
        Latte tallPSL2 = new Latte(tallPSL);

        LatteOrder order = new LatteOrder(3);

        // add tallPSL to the order
System.out.println(order.addLatte(tallPSL));

// add ventiPSL to the order
System.out.println(order.addLatte(ventiPSL));

// add ventiPSL2 to the order
System.out.println(order.addLatte(ventiPSL2));

// add tallPSL2 to the order – what happens here? 
System.out.println(order.addLatte(tallPSL2));

// are tallPSL and tallPSL2 the same? should be!
System.out.print("are tallPSL and tallPSL2 the same? ");
System.out.println(tallPSL.equals(tallPSL2));
// are tallPSL and ventiPSL the same? shouldn't be...
System.out.print("are tallPSL and ventiPSL the same? ");
System.out.println(tallPSL.equals(ventiPSL));

// Should call order’s toString methods
System.out.println(order);
    }


}