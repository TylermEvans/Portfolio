//Import Libraries
package lab01_TE;
import java.io.*;

//Database class
public class Database {
    //Instance Variables
    public Transaction mTransactions[] = new Transaction[9];
    protected int mSize = 0;
    protected String mFileName;
    //Class variables
    protected  static int msSizeIncrement = 20;




    //Consturctor. Takes a file name and loads the file. Parses the data and creates a transaction instance
    //for each line of the file.
    //Calls the addtransaction method and adds each transaction into the database
    public Database(String n)
    {

        mFileName = n;
        String notes = "";
        try
        {
            BufferedReader br = new BufferedReader(new FileReader(mFileName));
            String line = br.readLine();
            while (line != null)
            {


                line = line.trim();
                line = line.substring(1,line.length()-1);
                String[] elem = line.split(":");
                int id = Integer.parseInt(elem[0]);
                int account = Integer.parseInt(elem[1]);
                float amount = Float.parseFloat(elem[2].substring(1,elem[2].length()));
                if (elem.length > 3 )
                {
                    notes = elem[3];
                }
                Transaction t = new Transaction(id,account,amount,notes);
                addTransaction(t);



                line = br.readLine();
            }

        }
        catch (IOException e)

        {
            System.out.println("Error in reading file");

        }

    }
    //adds transaction instances into the mTransactions array of a database instance
    // Increases the size of the array if the maximum is reached
    public void addTransaction(Transaction t)
    {
        if (mTransactions.length == mSize)
       {
           int newsize = mSize+msSizeIncrement;
           Transaction L[] = new Transaction[newsize];
           System.arraycopy(mTransactions,0,L,0,mSize);
           mTransactions = L;
        }
        mTransactions[mSize] = t;
        mSize++;
    }
    //Sorts the transactions based on the parameter passed in. Calls the compare method to implement the bubble-sort algorithm
    public Transaction[] sortTransaction(int n)
    {
        boolean sorted = false;
        while (!sorted)
        {
            sorted = true;
            for (int i = 0;  i < mSize-1;  i++)
            {
                if (mTransactions[i].compare(mTransactions[i+1],n))
                {
                    Transaction temp = mTransactions[i+1];
                    mTransactions[i+1] = mTransactions[i];
                    mTransactions[i] = temp;
                    sorted = false;
                }
            }
        }
        return mTransactions;
    }
    // Removes a transaction instance from mTransactions based on id number
    public void removeTransaction(int id)
    {
        for (int i = 0; i <= mSize-1; i++)
        {
            if (mTransactions[i].getmID() == id)
            {
                System.arraycopy(mTransactions, i+1, mTransactions, i, mSize-i-1);


            }
        }
        mSize--;
    }
    //Saves the database data to a txt file. Used the same file name as before. If the file doesnt exists it
    //Auto-creates it
    public void saveDbase()
    {
        try
        {
            File f= new File("dbase2.txt");
            if (!f.exists())
                f.createNewFile();

            BufferedWriter bw = new BufferedWriter(new FileWriter(f));
            for (int i = 0; i <= mSize-1; i++)
            {
                bw.write(mTransactions[i] + "\n");
            }
            bw.close();
        }
        catch(IOException e)
        {
            System.out.println("error creating new file");
        }
    }
    //Getters
    public int getmSize() {
        return mSize;
    }
}
