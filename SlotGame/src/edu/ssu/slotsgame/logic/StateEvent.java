package edu.ssu.slotsgame.logic;


public class StateEvent extends GameEvent
{   private int state;
    private int prevState;

    public StateEvent(int type,int curstate,int prevstate) {
        super(type);
        state = curstate;
        prevState = prevstate;
    }

    public int getState()
    {
        return state;

    }
    public int getPrevState(){

        return prevState;
    }



}
