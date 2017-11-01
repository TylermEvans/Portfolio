package etec2101;

import java.util.ArrayList;

/**
 * This is our BinarySearchTree class. This class uses the BSTnode and the BSTiterator class. Most of the methods in this class
 * are wrapper methods. The bulk of the recursive work is done in the BSTnode class.
 * mRoot - the Root of the tree, or the first node in the tree
 * mSize - the Size of the Tree. Increases each time a new node is added
 * @param <E> - Takes a java generic value. Allows us to make a tree that can store any data type. Extends from Comparable
 */
public class BinarySearchTree<E extends Comparable>
{
    protected BSTnode mRoot;
    protected int mSize;


    /**
     * This constructor is very simple. Sets mSize to 0 initially and sets the mRoot to null
     * indicating that we have a empty tree
     */
    public BinarySearchTree()
    {
        mSize = 0;
        mRoot = null;


    }

    /**
     * This method takes a data value and makes a node with that value. Adds them by calling the BSTnode add method.
     * @param val - Takes a generic data value. Must be the same as the generic used when creating the tree
     */
    public void add(E val)
    {
        if (mRoot==null)
        {
            mRoot = new BSTnode(val);
        }
        else
        {
            mRoot.add(val);

        }
        mSize++;
    }

    /**
     * This method is a wrapper method. It calls getHeight from the BSTnode class on the Root of the tree
     * That method does the rest of the work.
     * @return - Returns the height of the tree
     */
    public int getHeight()
    {
        int val;
        val = mRoot.getHeight();
        return val;
    }

    /**
     * This method is a wrapper method. It calls the count method from the BSTnode class on the root of the tree
     * All of the work is handled there
     * @param val - Takes a generic data value
     * @return - Returns an integer indicating how many times a value appeared in the tree
     */
    public int count(E val)
    {
        int result;
        result =  mRoot.count(val);
        return result;
    }

    /**
     * This method uses the toStringHelper method in the BSTnode class. The toStringHelper does all of the heavy lifting to build
     * the String
     * @return - Returns the String representation of the BinarySearchTree class. Overides ToString
     */
    @Override
    public String toString()
    {
        if(mRoot!=null)
        {
            return mRoot.toStringHelper(0);

        }
        else
        {
            return "Nothing here";

        }
    }

    /**
     * These enums specify the traversaltype used for the BSTiterator
     */
    public enum TraversalType
    {
        In,Post,Pre
    }

    /**
     * A simple getter method that gets the root of the tree
     * @return - Returns root node
     */
    public  BSTnode getmRoot() {
        return mRoot;
    }

    /**
     * This methdo returns a BSTiterator.
     * @param root - The root of the tree
     * @param t - The TraversalType of the iteration
     * @return - Returns a BSTiterator
     */
    public BSTiterator iterator(BSTnode root,BinarySearchTree.TraversalType t)
    {
        return new BSTiterator(root,t);

    }

    /**
     * This method returns an ArrayList that holds the values of the tree in-order
     * @return - Returns an ArrayList
     */
    public ArrayList<E> toArray()
    {
        BSTiterator i = iterator(mRoot,TraversalType.In);
        return i.mValues;

    }

    /**
     * This method rebalances the tree. Uses a recursive method to do so.
     */
    public void rebalance()
    {
        mRoot = rebalanceRec(this.toArray());
    }

    /**
     *This mehtod is a recursive helper that does all of the work for the rebalance method.
     * This method rebalances the tree by recurisvely calling itself
     * @param a - Takes an initial ArrayList
     * @return - Returns a node that is the Root or a Subroot.
     */
    BSTnode<E> rebalanceRec(ArrayList<E> a)
    {

        int rootIndex = a.size()/2;
        BSTnode root = new BSTnode<E>(a.get(rootIndex));
        ArrayList<E> left = new ArrayList<E>();
        ArrayList<E> right = new ArrayList<E>();
        for (int i = 0; i<rootIndex; i++)
        {
            left.add(a.get(i));

        }

        for (int i = rootIndex+1; i<a.size(); i++)
        {
            right.add(a.get(i));

        }

        if(left.size()==1)
        {
            root.mLeft = new BSTnode(left.get(0));

        }
        else if(left.size()>1)
        {
            root.mLeft= rebalanceRec(left);

        }

        if(right.size()==1)
        {
            root.mRight= new BSTnode(right.get(0));

        }
        else if (right.size()>1)
        {
            root.mRight = rebalanceRec(right);

        }
        return root;


    }
}

