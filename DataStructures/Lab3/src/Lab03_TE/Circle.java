package Lab03_TE;
import org.newdawn.slick.*;

import java.util.Random;


public class Circle extends Shape
{
    protected int mRad;
    Random mGen = new Random();
    protected Color Col;



    public Circle(int x, int y, int r, int col[])
    {
        super(x,y,col,ShapeType.CIRCLE);
        mRad = r;
        mCol[0] = mGen.nextInt(255);
        mCol[1] = mGen.nextInt(255);
        mCol[2] = mGen.nextInt(255);
        Col = new Color(mCol[0],mCol[1],mCol[2]);
    }
    public void draw(Graphics g)
    {
        g.setColor(Col);
        g.fillOval(mXpos,mYpos,mRad,mRad);
    }

}
