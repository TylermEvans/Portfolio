package edu.ssu.slotsgame;
import javax.swing.*;

import edu.ssu.slotsgame.logic.*;
import edu.ssu.slotsgame.logic.CreditManager;

public class CreditLabel extends JLabel implements Observer
{

    public CreditLabel() {
        super("Credit: 0");
        this.setText("Credit: " + CreditManager.getInstance().getCurCredits());
        EventManager.getInstance().attach(this, GameEvent.CHANGE_STATE);
    }

    public void notify(GameEvent e)
    {
        StateEvent s = (StateEvent)e;
        if (s.getState()==GameState.SPIN){
            this.setText("Credits: " + CreditManager.getInstance().getCurCredits());
        }
        else{
            this.setText("Credits: " + CreditManager.getInstance().getCurCredits());
        }

    }

}