package edu.ssu.slotsgame.logic;


public class CreditManager
{
    public final static int INIT_CREDITS = 200;
    public final static CreditManager instance_ = new CreditManager();
    public int curCredits;

    public CreditManager(){
        curCredits = INIT_CREDITS;
    }
    public static CreditManager getInstance()
    {
        return instance_;


    }
    public void setCredits(int val)
    {
        this.curCredits = val;
    }
    public int getCurCredits(){
        return curCredits;
    }






}
