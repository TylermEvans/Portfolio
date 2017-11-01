package etec2101;


import java.util.ArrayList;
import org.newdawn.slick.*;
public class DrawableEdge<E>
{
    protected int scalex_fac = (1194-13)/1920;
    protected int scaley_fac = (786-8)/1080;
    protected int indA;
    protected int indB;
    protected E mData;
    protected DrawableNode node1;
    protected DrawableNode node2;
    protected ArrayList list;

    public DrawableEdge(int index1, int index2, E data, ArrayList L)
    {
        indA = index1;
        indB = index2;
        mData = data;
        list = L;
        node1 = (DrawableNode)list.get(indA);
        node2 = (DrawableNode)list.get(indB);
    }
    public void draw(Graphics g)
    {
        g.setColor(Color.white);
        g.drawLine(node1.mXpos,node1.mYpos,node2.mXpos,node2.mYpos);

    }

}
