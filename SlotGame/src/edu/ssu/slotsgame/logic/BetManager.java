package edu.ssu.slotsgame.logic;

import edu.ssu.slotsgame.config.GameParameters;
import edu.ssu.slotsgame.logic.*;

public class BetManager {

    public int curbet = 0;
    private final static BetManager instance_ = new BetManager();


    public void validateBet(int newbet, boolean change) {
        int constraint = getBetConstraints(change);
        if (change) {
            if (curbet == constraint) {
                curbet = constraint;
            } else {
                curbet++;
            }
        } else {
            if (curbet == constraint) {
                curbet = constraint;
            } else {
                curbet--;
            }
        }
    }

    public int getBetConstraints(boolean change) {
        GameParameters g = new GameParameters();
        if (change) {
            return g.MAX_BET;
        } else {
            return g.MIN_BET;
        }
    }

    public void increaseBet() {
        int prevbet;
        if (this.curbet!=GameParameters.MAX_BET)
        {
            prevbet = this.curbet;
        }
        else{
            prevbet = GameParameters.MAX_BET - 1;
        }
        validateBet(this.curbet, true);
        EventManager.getInstance().notify(new BetEvent(GameEvent.CHANGE_BET,this.curbet,prevbet));

    }

    public void decreaseBet() {
        int prevbet;
        if (this.curbet!=GameParameters.MIN_BET)
        {
            prevbet = this.curbet;
        }
        else{
            prevbet = GameParameters.MIN_BET + 1;
        }
        validateBet(this.curbet, false);
        EventManager.getInstance().notify(new BetEvent(GameEvent.CHANGE_BET,this.curbet,prevbet));
    }


    public static BetManager getInstance_()
    {
        return instance_;
    }


}


