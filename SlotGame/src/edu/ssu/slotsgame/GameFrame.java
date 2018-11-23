package edu.ssu.slotsgame;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

import edu.ssu.slotsgame.logic.*;
import edu.ssu.slotsgame.logic.BetManager;


public class GameFrame extends JFrame implements ActionListener {

    JPanel meterPanel;
    CreditLabel creditLabel;
    WonLabel wonLabel;
    BetLabel betLabel;

    JPanel buttonPanel;
    SpinButton spinButton;

    ReelPanel reelPanel;
    BetDownButton betDownButton;
    BetUpButton betUpButton;


    public GameFrame() {
        super("Slots Game");

        meterPanel = new JPanel(new BorderLayout());
        reelPanel = new ReelPanel();
        creditLabel = new CreditLabel();
        wonLabel = new WonLabel();
        wonLabel.setHorizontalAlignment(SwingConstants.CENTER);

        betLabel = new BetLabel();

        meterPanel.add(creditLabel, BorderLayout.WEST);
        meterPanel.add(wonLabel, BorderLayout.CENTER);
        meterPanel.add(betLabel, BorderLayout.EAST);

        this.add(meterPanel, BorderLayout.NORTH);
        this.add(reelPanel,BorderLayout.CENTER);

        buttonPanel = new JPanel(new BorderLayout());
        spinButton = new SpinButton("SPIN");
        spinButton.addActionListener(this);

        buttonPanel.add(spinButton, BorderLayout.CENTER);
        betUpButton = new BetUpButton("BetUp");
        betDownButton = new BetDownButton("BetDown");
        betDownButton.addActionListener(this);
        betUpButton.addActionListener(this);
        buttonPanel.add(betUpButton,BorderLayout.EAST);
        buttonPanel.add(betDownButton,BorderLayout.WEST);


        this.add(buttonPanel, BorderLayout.SOUTH);

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(640, 480);
        this.setVisible(true);
    }

    public void actionPerformed(ActionEvent event)
    {
        if (event.getActionCommand().equals("SPIN")){

           GameStateManager.getInstance_().setCurrentState_(GameState.PRESPIN);

       }
       if(event.getActionCommand().equals("BetUp")) {

           BetManager.getInstance_().increaseBet();

       }
       if (event.getActionCommand().equals("BetDown")){
           BetManager.getInstance_().decreaseBet();
       }



    }


}