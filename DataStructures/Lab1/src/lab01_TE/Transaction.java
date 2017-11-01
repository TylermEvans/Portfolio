package lab01_TE;
//Transaction class
public class Transaction {

    //Instance Variables
    protected int mID;
    protected int mAccount;
    protected float mAmount;
    protected String mNotes;
    //Class variables
    protected static int msID = 1;




    //Initial constructor that takes id, account amount and notes as parameters
    public Transaction(int a,int b, float c, String d)
    {

        mID = a;
        mAccount = b;
        mAmount = c;
        mNotes = d;
        if (msID < mID+1)
        {
            msID = mID+1;

        }





    }
    //Second constructor that auto-creates the id number
    public Transaction(int a, float b, String c)
    {


        mID = msID;
        mAccount = a;
        mAmount = b;
        mNotes = c;
        msID++;


    }
    //Overides the print method for transactions. Returns it in this form.
    public String toString()

    {
        return "[" + this.mID + ":" + this.mAccount + ":" + this.mAmount + ":" + this.mNotes + "]";

    }
    //Compares two transactions. The int passed in represents what instance variable to compare upon
    //returns a boolean
    public boolean compare(Transaction t, int n)
    {
        if (n == 1) {
            if (this.mID > t.mID) {
                return true;
            }
        }
        if (n == 2) {
            if (this.mAccount > t.mAccount) {
                return true;
            }
        }
        if (n == 3) {
            if (this.mAmount > t.mAmount) {
                return true;
            }
        }
        if (n == 4) {
            if (this.mNotes.length() > t.mNotes.length()) {
                return true;
            }
        }
        return false;
    }

    //Getters
    public int getmID()
    {
        return mID;
    }

    public static int getMsID()
    {
        return msID;
    }


    public int getmAccount()
    {
        return mAccount;
    }

    public float getmAmount() {

        return mAmount;
    }

    public String getmNotes() {
        return mNotes;
    }

}
