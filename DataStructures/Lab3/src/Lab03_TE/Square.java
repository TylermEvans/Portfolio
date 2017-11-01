package Lab03_TE;
import org.newdawn.slick.*;

import java.util.Random;

public class Square extends Shape
{
    protected int mSize;
    Random mGen = new Random();
    protected Color Col;

    public Square(int x, int y, int s, int col[])
    {
        super(x,y,col,ShapeType.SQUARE);
        mSize = s;
        mCol[0] = mGen.nextInt(255);
        mCol[1] = mGen.nextInt(255);
        mCol[2] = mGen.nextInt(255);
        Col = new Color(mCol[0],mCol[1],mCol[2]);
    }
    public void draw(Graphics g)
    {
        g.setColor(Col);
        g.fillRect(mXpos,mYpos,mSize,mSize);

    }


}
