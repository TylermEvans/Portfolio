package etec2101;
import java.util.*;
import java.io.*;
import org.newdawn.slick.*;
public class DrawableGraph extends Graph<DrawableNode, DrawableEdge>
{

    ArrayList<DrawableNode> mPoints = new ArrayList<>();
    public DrawableGraph(String fname)
    {
        try
        {
            Scanner s = new Scanner(new File(fname));
            while(s.hasNextLine())
            {
                String line = s.nextLine();
                line = line.trim();
                String[] parts = line.split(" ");

                if (parts[0].equals("n"))
                {
                    DrawableNode n = new DrawableNode(Integer.parseInt(parts[2]),Integer.parseInt(parts[3]),Integer.parseInt(parts[4]));
                    this.addNode(n);
                    mPoints.add(n);
                }
                if (parts[0].equals("e"))
                {
                    DrawableEdge e = new DrawableEdge(Integer.parseInt(parts[1]),Integer.parseInt(parts[2]),parts[3],mPoints);
                    this.addEdge(e,mPoints.get(e.indA),mPoints.get(e.indB),true);
                }
            }
        }
        catch(FileNotFoundException e) {
            System.out.println("Not here");

        }

    }
    public void draw(Graphics g)
    {
        HashMap.HashMapIterator i = mGraph.iterator(HashMap.IteratorType.KEY);
        while(i.hasNext())
        {
            DrawableNode mCurNode = (DrawableNode) i.next();
            HashMap tmp = mGraph.get(mCurNode);
            HashMap.HashMapIterator i2 = tmp.iterator(HashMap.IteratorType.KEY);
            while (i2.hasNext())
            {
                DrawableNode mCurNode2 = (DrawableNode)i2.next();
                DrawableEdge e = (DrawableEdge)tmp.get(mCurNode2);
                e.draw(g);
            }
            mCurNode.draw(g);


        }
    }

    public DrawableNode startNode(int x , int y)
    {
        DrawableNode result = null;
        HashMap.HashMapIterator i = mGraph.iterator(HashMap.IteratorType.KEY);
        while(i.hasNext())
        {
            DrawableNode mCur = (DrawableNode)i.next();
            double distance = Math.pow((Math.pow(mCur.mXpos-x,2) + Math.pow(mCur.mYpos-y,2)),0.5);
            if (distance<mCur.mRad)
            {
                result = mCur;
                System.out.println("hit");

            }
        }

        return result;
    }

    public void dfs(DrawableNode startNode, HashMap parentMap, Graph graph)
    {
        DrawableNode newSnode = null;
        HashMap.HashMapIterator i = graph.mGraph.iterator(HashMap.IteratorType.KEY);
        while (i.hasNext())
        {
            DrawableNode n = (DrawableNode)i.next();

            if (!parentMap.inMap(n))
            {
                parentMap.set(n, startNode);
                newSnode = n;
                dfs(newSnode,parentMap,graph);
            }
            else
            {
                break;

            }
        }

    }

}
