package etec2101;
import org.newdawn.slick.*;
import org.newdawn.slick.geom.Ellipse;


public class DrawableNode<N>
{

    protected int mXpos;
    protected int mYpos;
    protected int mRad;


    public DrawableNode(int x, int y, int rad)
    {
        mXpos = x;
        mYpos = y;
        mRad = rad;
    }
    public void draw(Graphics g)
    {
        g.setColor(Color.white);
        g.fill(new Ellipse(mXpos,mYpos,mRad,mRad));


    }
}
