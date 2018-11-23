package edu.ssu.slotsgame;
import edu.ssu.slotsgame.logic.*;
import edu.ssu.slotsgame.config.*;

import javax.swing.*;


public class BetDownButton extends JButton implements Observer {


    public BetDownButton(String text)
    {
        super(text);
        EventManager.getInstance().attach(this,GameEvent.CHANGE_BET);

    }

    public void notify(GameEvent e)
    {
        BetEvent b = (BetEvent)e;
        if (b.getBetAmount()==GameParameters.MIN_BET){
            this.setEnabled(false);
        }
        else{
            this.setEnabled(true);
        }
    }


}
