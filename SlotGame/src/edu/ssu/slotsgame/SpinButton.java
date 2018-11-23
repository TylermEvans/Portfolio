package edu.ssu.slotsgame;


import edu.ssu.slotsgame.logic.*;

import javax.swing.*;
import java.security.cert.CRLException;

public class SpinButton extends JButton implements Observer
{



    public SpinButton(String text)
    {
        super(text);
        EventManager.getInstance().attach(this,GameEvent.CHANGE_STATE);


    }

    public void notify(GameEvent e)
    {
        StateEvent s = (StateEvent)e;
        if (s.getState()==GameState.PRESPIN)
        {

            if (BetManager.getInstance_().curbet<=CreditManager.getInstance().getCurCredits() && BetManager.getInstance_().curbet!=0){
                int result = CreditManager.getInstance().getCurCredits() - BetManager.getInstance_().curbet;
                CreditManager.getInstance().setCredits(result);
                GameStateManager.getInstance_().setCurrentState_(GameState.SPIN);
                System.out.println("Setting state to SPIN");
            }
            else{
                GameStateManager.getInstance_().setCurrentState_(GameState.READY);
            }

        }
        else if (s.getState()==GameState.SPIN){
            this.setEnabled(false);
        }
        else{
            this.setEnabled(true);
        }

    }


}
