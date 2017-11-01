package lab04_TE;
import etec2101.*;
//import etec2101.BinarySearchTreeIterator;
import java.util.*;
public class Main
{
    public static void main(String[] args)
    {
        BinarySearchTree<String> T = new BinarySearchTree();
        T.add("monkey");
        T.add("gorilla");
        T.add("cougar");
        T.add("jaguar");
        T.add("dog");
        T.add("aardvark");
        T.add("zebra");
        T.add("tortoise");
        T.add("unicorn");
        System.out.println("T =\n" + T);

        System.out.println("Height(T) = " + T.getHeight());

        //T.remove("unicorn");
        //System.out.println("T (after removing 'unicorn') = \n" + T);

        //T.remove("cougar");
        //System.out.println("T (after removing 'cougar') = \n" + T);
        //T.remove("monkey");
        // System.out.println("T (after removing 'monkey') = \n" + T);
         T.add("dog");
        System.out.println("There are " + T.count("dog") + " \"dog's\" in T");
        System.out.println("There are " + T.count("tortoise") +
        " \"tortoises's\" in T");
         System.out.println("There are " + T.count("wolf") + " \"wolf's\" in T");

        System.out.println("T = \n" + T);

         System.out.println("In-order traversal of T\n=======================");
         Iterator I = T.iterator(T.getmRoot(),BinarySearchTree.TraversalType.In);
         while (I.hasNext())
        {
            Object s = I.next();
            System.out.println("\t" + s);
         }

        BinarySearchTree<Double> U = new BinarySearchTree();
         U.add(13.2);
         U.add(19.7);
         U.add(23.4);
         U.add(16.4);
          U.add(29.8);
          U.add(32.6);
           U.add(42.0);
          U.add(41.0);
          U.add(53.0);
         U.add(68.3);
         U.add(72.5);
          System.out.println("U = \n" + U);
        U.rebalance();
        System.out.println("U (after rebalance) = \n" + U);

         System.out.println("pre-order traversal of U\n========================");
         I = U.iterator(U.getmRoot(),BinarySearchTree.TraversalType.Pre);
         while (I.hasNext())
            System.out.println("\t" + I.next().toString());

         System.out.println("post-order traversal of U\n=========================");
         I = U.iterator(U.getmRoot(),BinarySearchTree.TraversalType.Post);
         while (I.hasNext())
             System.out.println("\t" + I.next().toString());
        System.out.println(T.toArray());
    }
}
