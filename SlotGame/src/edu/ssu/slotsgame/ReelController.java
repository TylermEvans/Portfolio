package edu.ssu.slotsgame;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;

import edu.ssu.slotsgame.logic.EventManager;
import edu.ssu.slotsgame.logic.GameEvent;
import edu.ssu.slotsgame.logic.Observer;
import edu.ssu.slotsgame.logic.*;

public class ReelController {
    private static ReelController instance = new ReelController();



    public void update( ReelStrip[] reels,GameEvent e)
    {
        StateEvent s = (StateEvent)e;


        if (s.getState()==GameState.SPIN)
        {
            for (int k = 0; k < 3; ++k)
            {
                reels[k].spinning = true;
            }



        }
        else if (s.getState()==GameState.POSTSPIN)
        {
            int won = evaluate(reels);
            CreditManager.getInstance().setCredits(CreditManager.getInstance().getCurCredits()+won);

            GameStateManager.getInstance_().setCurrentState_(GameState.READY);


        }
        else {

        }
    }


    public int evaluate(ReelStrip[] reels)
    {
        String matchedSymbol = reels[0].getReelSymbol().getSymName();
        int matchCount = 1;
        for (int i = 1; i <reels.length; ++i) {
            if (reels[i].getReelSymbol().getSymName().equals(matchedSymbol))
                matchCount++;
            else
                break;
        }

        int payout = PayTable.getInstance().getPayout(
                matchedSymbol,
                matchCount);


        return payout;
    }






    public static ReelController getInstance(){
        return instance;
    }




}
