package edu.ssu.slotsgame;
import edu.ssu.slotsgame.logic.*;
import edu.ssu.slotsgame.config.*;

import javax.swing.*;

public class BetUpButton extends JButton implements Observer
{
    public BetUpButton(String text){
        super(text);
        EventManager.getInstance().attach(this,GameEvent.CHANGE_BET);

    }
    public void notify(GameEvent e){

        BetEvent b = (BetEvent)e;
        if (b.getBetAmount()==GameParameters.MAX_BET){
            this.setEnabled(false);
        }
        else{
            this.setEnabled(true);
        }



    }

}
