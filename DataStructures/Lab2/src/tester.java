package Lab02;

import etec2101.LinkedList;
import etec2101.LinkedList.LinkedListIterator;
import java.util.Iterator;


public class tester
{
    public static void main(String[] args)
    {
        // Test the basics.
        LinkedList<String> L = new LinkedList<String>();
        L.addToBegin("Bob");
        L.addToEnd("Doug");
        L.addToBegin("Abe");
        System.out.println("L = " + L);                     // L = <[Abe][Bob][Doug]>

        // Test the indexing-like capabilities of our LinkedList
        System.out.println("L[0] = " + L.at(0, true));      // L[0] = Abe
        System.out.println("L[-1] = " + L.at(0, false));    // L[-1] = Doug
        System.out.println("L[2] = " + L.at(2));            // L[2] = Doug

        // Test the insert operator
        L.insert(1, "Sue");
        System.out.println("L = " + L);                     // L = <[Abe][Sue][Bob][Doug]>
        L.insert(0, "Chris");
        System.out.println("L = " + L);                     // L = <[Chris][Abe][Sue][Bob][Doug]>
        L.insert(5, "Xavier");
        System.out.println("L = " + L);                     // L = <[Chris][Abe][Sue][Bob][Doug][Xavier]>
        L.insert(3, "Chris");
        System.out.println("L = " + L);                     // L = <[Chris][Abe][Sue][Chris][Bob][Doug][Xavier]>
        System.out.println("L.length() = " + L.length());   // L.length() = 7

        // Test the count and removeAll method
        System.out.println(L.count("Chris"));               // 2
        System.out.println(L.removeAll("Chris"));           // 2
        System.out.println("L = " + L);                     // L = <[Abe][Sue][Bob][Doug][Xavier]>
        System.out.println("L.length() = " + L.length());   // L.length() = 5

        // Test the forward and backwards iterator (this has the nice benefit of testing your pointers too)
        // You figure out if you have the right results:-)
        System.out.println("Forward iterator\n================");
        LinkedList<String>.LinkedListIterator LI = L.iterator();
        while (LI.hasNext())
        {
            String s = LI.next();
            System.out.println("\t" + s);
        }
        System.out.println("Backwards iterator\n==================");
        LI = L.riterator();
        while (LI.hasNext())
        {
            String s = LI.next();
            System.out.println("\t" + s);
        }


        // Quickly proving that we can use other types as well as string
        LinkedList<Double> L2 = new LinkedList<Double>();
        L2.addToEnd(15.3);
        L2.addToBegin(37.9);
        L2.addToEnd(19.4);
        L2.removeAll(15.3);
        System.out.println("L2 = " + L2);           // L2 = <[37.9][19.4]>
    }
}