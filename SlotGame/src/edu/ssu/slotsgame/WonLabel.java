package edu.ssu.slotsgame;
import javax.swing.*;

import edu.ssu.slotsgame.logic.*;

public class WonLabel extends JLabel implements Observer {

    public WonLabel() {
        super("Won: 0");

        EventManager.getInstance().attach(this, GameEvent.CHANGE_BET);
    }

    public void notify(GameEvent e) {
        this.setText("Won: -999999");
    }
}