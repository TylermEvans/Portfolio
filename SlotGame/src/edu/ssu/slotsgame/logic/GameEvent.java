package edu.ssu.slotsgame.logic;

public class GameEvent
{
    public final static int NONE = 0;
    public final static int CHANGE_BET = 1;
    public final static int CHANGE_STATE = 2;

    private int type_;



    public GameEvent(int type)
    {
        type_ = type;
    }

    public int getType()
    {
        return type_;
    }
}