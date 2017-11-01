import lab01_TE.Transaction;
import lab01_TE.Database;


public class MainClass {

    public static void main(String[] args)
    {
        //Creates two transaction instances
        Transaction t = new Transaction(1,1222,3333,"Money, money");
        Transaction n = new Transaction(2,2222,4444,"Money, money 2.0");
        Transaction z = new Transaction(5000,5000,"yeah");
        //Shows off the toString method
        System.out.println(t);
        System.out.println(n);
        //Shows off the constructor overide
        System.out.println(z);
        //compares the id, should be false
        System.out.println(t.compare(n,1));
        //compares the account numbers, should be true
        System.out.println(n.compare(t,2));

        //loads the database
        Database d = new Database("dbase.txt");

        //prints out the data in the database txt file
        for (int i = 0; i <= d.getmSize()-1; i++)
        {
            System.out.println(d.mTransactions[i]);

        }
        //Tests the addtransaction method
        Transaction f = new Transaction(9,3000,3000,"yeah");
        d.addTransaction(f);
        //Makes a new space
        System.out.println("");
        //Should have a new transaction on the end
        for (int i = 0; i <= d.getmSize()-1; i++)
        {
            System.out.println(d.mTransactions[i]);

        }
        //Sorts the transactions in the database
        d.sortTransaction(1);
        //Space
        System.out.println("");

        for (int i = 0; i <= d.getmSize()-1; i++)
        {
            System.out.println(d.mTransactions[i]);

        }
        //removes the transaction with a 0 id number
        d.removeTransaction(5);

        System.out.println("");

        for (int i = 0; i <= d.getmSize()-1; i++)
        {
            System.out.println(d.mTransactions[i]);

        }

        d.saveDbase();



    }



}
