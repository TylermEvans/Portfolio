package Lab03_TE;
import org.newdawn.slick.*;

public class Shape
{
    protected int mXpos;
    protected int mYpos;
    protected int[] mCol;
    protected ShapeType mType;


    public Shape(int x, int y, int[] col,ShapeType t)
    {
        mXpos = x;
        mYpos = y;
        mCol = col;
        mType = t;

    }
    enum ShapeType
    {
        CIRCLE,SQUARE

    }

    /**
     * Draws a shape onto a slick2d graphics object based on what shape is being used.
     * @param g - A slick2d graphics object
     */
    public void draw(Graphics g)
    {

    }


    /**
     *
     * @return returns the type of a shape
     */
    public ShapeType getmType() {
        return mType;
    }

    /**
     *
     * @return returns the x position of a shape
     */
    public int getmXpos()
    {
        return mXpos;
    }

    /**
     *
     * @return returns a y position of a shape
     */
    public int getmYpos()
    {
        return mYpos;
    }

}

