package edu.ssu.slotsgame;

import java.util.*;
import java.awt.*;
import java.awt.image.*;
import java.io.File;
import javax.imageio.ImageIO;

public class ReelStrip {

    public static HashMap<String, BufferedImage> imageMap = null;
    public static float doffset;
    public static int gap = 5;
    public static int symbolWidth;
    public static int symbolHeight;


    static {
        imageMap = new HashMap<>();

        try {
            BufferedImage symbolImg = ImageIO.read(new File("simage.png"));
            BufferedImage[][] symbols = new BufferedImage[3][3];
            int width = symbolImg.getWidth() / 3;
            int height = symbolImg.getHeight() / 3;

            symbolWidth = width;
            symbolHeight = height;

            for (int row = 0; row < 3; ++row) {
                for (int col = 0; col < 3; ++col) {
                    symbols[row][col] = symbolImg.getSubimage(width * col,
                            height * row, width, height);
                }
            }

            imageMap.put("watermelon", symbols[0][0]);
            imageMap.put("bell", symbols[0][1]);
            imageMap.put("seven", symbols[0][2]);

            imageMap.put("lime", symbols[1][0]);
            imageMap.put("cherry", symbols[1][1]);
            imageMap.put("plum", symbols[1][2]);

            imageMap.put("grapes", symbols[2][0]);
            imageMap.put("orange", symbols[2][1]);
            imageMap.put("bar", symbols[2][2]);

            doffset = height / 200.0f;
        } catch (Exception e) {
            System.err.println(e);
            System.exit(0);
        }
    }

    public ArrayList<ReelSymbol> symbolList;

    public int x = 0;
    public int y = 0;
    public int index = 0;
    public boolean spinning = false;
    public int timeUntilStop = 1500;

    public float offset = 0.0f;

    public ReelStrip() {
        symbolList = new ArrayList<>();
        symbolList.add(new ReelSymbol("bell"));
        symbolList.add(new ReelSymbol("cherry"));
        symbolList.add(new ReelSymbol("watermelon"));
        symbolList.add(new ReelSymbol("bar"));
    }

    public void paint(int reelX, int reelY, Graphics g) {

        // render center symbol
        BufferedImage centerSymbol = imageMap.get(symbolList.get(index).getSymName());
        g.drawImage(centerSymbol, x, y + symbolHeight + (int)offset, null);

        // render top/next symbols
        BufferedImage topSymbol = null;
        BufferedImage nextSymbol = null;
        if (index - 1 == -1) {
            topSymbol = imageMap.get(symbolList.get(symbolList.size() - 1).getSymName());
            nextSymbol = imageMap.get(symbolList.get(symbolList.size() - 2).getSymName());
        } else if (index - 1 == 0) {
            topSymbol = imageMap.get(symbolList.get(index - 1).getSymName());
            nextSymbol = imageMap.get(symbolList.get(symbolList.size() - 1).getSymName());
        } else {
            topSymbol = imageMap.get(symbolList.get(index - 1).getSymName());
            nextSymbol = imageMap.get(symbolList.get(index - 2).getSymName());
        }

        g.drawImage(topSymbol, x, y + (int)offset, null);
        g.drawImage(nextSymbol, x, y - symbolHeight + (int)offset, null);

        BufferedImage bottomSymbol = null;
        if (index + 1 == symbolList.size()) {
            bottomSymbol = imageMap.get(symbolList.get(0).getSymName());
        } else {
            bottomSymbol = imageMap.get(symbolList.get(index + 1).getSymName());
        }

        g.drawImage(bottomSymbol, x, y + symbolHeight * 2 + (int)offset, null);
    }
    public ReelSymbol getReelSymbol(){
        return this.symbolList.get(index);
    }
}