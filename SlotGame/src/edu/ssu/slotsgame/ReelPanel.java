package edu.ssu.slotsgame;

import edu.ssu.slotsgame.logic.EventManager;
import edu.ssu.slotsgame.logic.Observer;
import edu.ssu.slotsgame.logic.*;
import java.util.Random;




import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import javax.imageio.ImageIO;
import java.io.*;



public class ReelPanel extends JPanel implements ActionListener,Observer
{


    BufferedImage symbolMap;
    javax.swing.Timer timer;
    ReelStrip[] reels;
    int reelX = 100;
    int reelY = 15;
    int counter = 1000000;

    public ReelPanel()
    {
        reels = new ReelStrip[3];

        int width = ReelStrip.symbolWidth;
        for (int i = 0; i < 3; ++i)
        {
            reels[i] = new ReelStrip();
            reels[i].x = reelX + i * (width + ReelStrip.gap);
            reels[i].y = reelY;
        }
        EventManager.getInstance().attach(this,GameEvent.CHANGE_STATE);


        timer = new javax.swing.Timer(20, this);
        timer.start();



    }

    public void actionPerformed(ActionEvent e)
    {

        for (int i = 0; i < 3; ++i) {
            if (reels[i].spinning) {
                Random rand = new Random();
                int  n = rand.nextInt(50) + 20;
                reels[i].offset += ReelStrip.doffset * n;
                while (reels[i].offset >= ReelStrip.symbolHeight) {
                    reels[i].offset -= ReelStrip.symbolHeight;
                    reels[i].index -= 1;
                    if (reels[i].index < 0) {
                        reels[i].index += reels[i].symbolList.size();
                    }
                }

                reels[i].timeUntilStop -= 20;
                if (reels[i].timeUntilStop <= 0) {
                    reels[i].spinning = false;
                    reels[i].timeUntilStop = 1500;
                    if (i == 2) {
                        GameStateManager.getInstance_().setCurrentState_(GameState.POSTSPIN);
                    }
                }


            } else {

                reels[i].offset = ReelStrip.doffset + 0;


            }


        }

        int width = getSize().width;
        int height = getSize().height;
        this.paintImmediately(0, 0, width, height);



    }
    public void notify(GameEvent e)
    {



        ReelController.getInstance().update(reels,e);

    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.setClip(reelX, reelY, ReelStrip.symbolWidth * 3 + ReelStrip.gap * 2,
                ReelStrip.symbolHeight * 3);
        for (int i = 0; i < 3; ++i) {
            reels[i].paint(reelX, reelY, g);
        }
    }
    public int evaluate()
    {
        String matchedSymbol = this.reels[0].getReelSymbol().getSymName();
        int matchCount = 1;
        for (int i = 1; i < this.reels.length; ++i) {
            if (this.reels[i].getReelSymbol().getSymName().equals(matchedSymbol))
                matchCount++;
            else
                break;
        }

        int payout = PayTable.getInstance().getPayout(
                matchedSymbol,
                matchCount);


        return payout;
    }

}