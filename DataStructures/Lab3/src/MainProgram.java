import java.util.logging.*;

import Lab03_TE.Shape;
import Lab03_TE.Circle;
import Lab03_TE.Square;
import etec2101.LinkedList;
import org.newdawn.slick.*;
import etec2101.Stack;
import etec2101.Queue;


public class MainProgram extends BasicGame implements MouseListener,KeyListener
{
    //Variables
    public Shape curShape;
    public int shapeType = 2;
    public int mouseX;
    public int mouseY;
    public float rad = 50;
    public int[] color = new int[3];
    public int newX;
    public int newY;
    public int mouseWheel;
    public Stack<Shape> mUndo = new Stack<Shape>();
    public Stack<Shape> mRedo = new Stack<Shape>();
    public Queue<String> mLog = new Queue<String>();
    public String x1,x2,x3,x4;
    public Color stringCol;
    public int alpha = 255;
    public int alphaStart;
    public boolean control=false;
    public MainProgram(String gamename)
    {
        super(gamename);
    }
    @Override
    //Init for the gamecontainer object
    public void init(GameContainer gc) throws SlickException
    {
        gc.getInput().addKeyListener(this);
        gc.getInput().addMouseListener(this);

    }
    @Override
    //Key event handling - released
    public void keyReleased(int key, char c)
    {
        if (key==Input.KEY_LCONTROL)
        {
            control = false;
        }
    }

    @Override
    //Key event handling - pressed
    public void keyPressed(int key, char c)
    {
        if (key==Input.KEY_1)
        {
            shapeType = 1;

        }

        if (key==Input.KEY_2)
        {
            shapeType = 2;
        }
        if (key==Input.KEY_LCONTROL)
        {
            control = true;
        }

        if (control)
        {
            if (key==Input.KEY_Z && mUndo.getmList().length()>0)
            {
                Shape temp = mUndo.peek();
                mUndo.pop();
                mRedo.push(temp);
                alpha = 255;
                mLog.push("--UNDO-->");

            }
            if (key==Input.KEY_Y && mRedo.getmList().length()>0)
            {
                Shape temp = mRedo.peek();
                mRedo.pop();
                mUndo.push(temp);
                alpha = 255;
                mLog.push("<--REDO--");
            }

        }
    }

    @Override
    //Mouse movement
    public void mouseMoved(int oldx, int oldy, int newx, int newy)
    {
        newX = newx;
        newY = newy;

    }
    @Override
    //Mouse wheel movement
    public void mouseWheelMoved(int change)
    {
        mouseWheel = change;
        rad = rad+change*0.01f;
        System.out.println(change);
        if (rad<=5)
        {
            rad = 5;
        }
        if (rad>=50)
        {
            rad = 50;
        }

    }
    @Override
    //Mouse click input
    public void mousePressed(int button, int x, int y)
    {

        mouseX = x;
        mouseY = y;
        if (button==0 && shapeType==1)
        {
            curShape = new Circle(mouseX, mouseY, (int)rad, color);
            mUndo.push(curShape);
            mLog.push("Circle placed at ( "+mouseX+" , "+mouseY+ " )");
            alpha = 255;


        }
        if (button==0 && shapeType==2)
        {
            curShape = new Square(mouseX,mouseY,(int)rad,color);
            mUndo.push(curShape);
            mLog.push("Square placed at ( "+mouseX+" , "+mouseY+" ) ");
            alpha = 255;
        }

    }
    @Override
    public void update(GameContainer gc, int i) throws SlickException {


    }
    @Override
    //renders the graphical data
    public void render(GameContainer gc, Graphics g) throws SlickException
    {
        if (shapeType==1)
        {
            Color temp = new Color(255,255,255);
            g.setColor(temp);
            g.drawOval(newX,newY,rad,rad);
        }
        else
        {
            Color temp = new Color(255,255,255);
            g.setColor(temp);
            g.drawRect(newX,newY,rad,rad);
        }
        for (int i = 0; i<mUndo.getmList().length(); i++)
        {
            mUndo.getmList().at(i).draw(g);
        }
        if (mLog.length()>0)
        {
            x4 = x3;
            x3 = x2;
            x2 = x1;
            x1 = mLog.pop();
        }
        if (x4!=null)
        {
            alphaStart = 150;
            stringCol = new Color(255,255,255,alpha-alphaStart);
            g.setColor(stringCol);
            g.drawString(x4, 300, 320);
        }
        if (x3!=null)
        {
            alphaStart = 100;
            stringCol = new Color(255,255,255,alpha-alphaStart);
            g.setColor(stringCol);
            g.drawString(x3,300,340);
        }
        if (x2!=null)
        {
            alphaStart = 50;
            stringCol = new Color(255,255,255,alpha-alphaStart);
            g.setColor(stringCol);
            g.drawString(x2,300,360);
        }
        if (x1!=null)
        {
            alphaStart = 0;
            stringCol = new Color(255,255,255,alpha-alphaStart);
            g.setColor(stringCol);
            g.drawString(x1,300,380);
        }
        alpha-=0.001;












    }
    //The main method, runs and maintains the slick2d game
    public static void main(String[] args)
    {
        try
        {
            AppGameContainer appgc;
            appgc = new AppGameContainer(new MainProgram("Simple Slick Game"));
            appgc.setDisplayMode(640, 480, false);
            appgc.start();
        }
        catch (SlickException ex)
        {
            Logger.getLogger(MainProgram.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}