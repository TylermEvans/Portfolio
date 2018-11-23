package edu.ssu.slotsgame.logic;


public class BetEvent extends GameEvent
{
    private int betAmount;
    private int prevBetAmount;

    public BetEvent(int type,int betAmount,int prevBetAmount){
        super(type);
        this.betAmount = betAmount;
        this.prevBetAmount = prevBetAmount;


    }
    public int getBetAmount(){

        return betAmount;
    }
    public int getPrevBetAmount(){
        return prevBetAmount;
    }

}
