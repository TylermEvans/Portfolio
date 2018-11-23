package edu.ssu.slotsgame;
import javax.swing.*;

import edu.ssu.slotsgame.logic.*;

public class BetLabel extends JLabel implements Observer {

    public BetLabel() {
        super("Bet: 0");
        EventManager.getInstance().attach(this, GameEvent.CHANGE_BET);
    }

    public void notify(GameEvent e)
    {
        BetEvent b = (BetEvent) e;
        this.setText("Bet: " + b.getBetAmount());
    }
}
