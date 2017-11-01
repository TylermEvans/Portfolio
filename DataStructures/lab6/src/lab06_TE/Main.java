package lab06_TE;
import etec2101.*;

import java.util.logging.*;

import org.newdawn.slick.*;


public class Main extends BasicGame implements MouseListener,KeyListener
{
    DrawableGraph mGraph = new DrawableGraph("map04.txt");
    HashMap parentMap = new HashMap(50,0.7f,50);
    DrawableNode n;

    public Main(String gamename)
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

    }

    @Override
    //Key event handling - pressed
    public void keyPressed(int key, char c)
    {
        if (key==Input.KEY_D)
        {
            mGraph.dfs(n,parentMap,mGraph);

        }

    }

    @Override
    //Mouse movement
    public void mouseMoved(int oldx, int oldy, int newx, int newy)
    {

    }

    @Override
    //Mouse click input
    public void mousePressed(int button, int x, int y)
    {
        DrawableNode n = mGraph.startNode(x,y);
        parentMap.set(n,null);





    }
    @Override
    public void update(GameContainer gc, int i) throws SlickException {


    }
    @Override
    //renders the graphical data
    public void render(GameContainer gc, Graphics g) throws SlickException
    {
        mGraph.draw(g);




    }
    //The main method, runs and maintains the slick2d game
    public static void main(String[] args)
    {
        try
        {
            AppGameContainer appgc;
            appgc = new AppGameContainer(new Main("Simple Slick Game"));
            appgc.setDisplayMode(1920, 1080, false);
            appgc.start();
        }
        catch (SlickException ex)
        {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}