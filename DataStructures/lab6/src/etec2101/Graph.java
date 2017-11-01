package etec2101;


import java.util.ArrayList;

public class Graph<N,E>
{

    protected HashMap<N,HashMap<N,E>> mGraph;
    protected ArrayList mNodes = new ArrayList();
    protected ArrayList mEdges = new ArrayList();

    public Graph()
    {
        mGraph = new HashMap<N, HashMap<N, E>>(50,0.7f,50);

    }

    public void addNode(N val)
    {
        mGraph.set(val, new HashMap<N, E>(10,0.7f,10));

    }

    public void addEdge(E data, N nodeA, N nodeB, boolean bidirectional)
    {
        mGraph.get(nodeA).set(nodeB,data);


    }





}
