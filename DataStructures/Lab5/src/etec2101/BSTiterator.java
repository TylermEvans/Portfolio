package etec2101;


import java.util.ArrayList;
import java.util.Iterator;

/**
 * This Class is the iterator for the BinarySearchTree. Can only be created internally by calling the iteraotr method in the BinarySearchTree.
 * @param <E> - Takes a java generic if you wish to use an Iterator of only a certain type. Normally not used. Extends from Comparable
 */
class BSTiterator<E extends Comparable > implements Iterator<E>
{
    ArrayList<E> mValues;
    int mCur;
    BinarySearchTree.TraversalType type;


    /**
     * The constructor saves the Traversal type and creates an empty ArrayList.
     * Calls the builArrayList method on the root node. buildArrayList fills the mValues ArrayList with the values of the tree based on
     * the Traversal Type
     * @param root - A BinarySearchTree Node. Normally the Root of the tree.
     * @param t - The traversal type of the iteration.
     */
    protected BSTiterator(BSTnode root, BinarySearchTree.TraversalType t)
    {
        type = t;
        mValues = new ArrayList<E>();
        root.buildArrayList(mValues,type);
    }


    /**
     * This method returns where we are in our iteration.
     * @return - Returns a boolean.
     */
    @Override
    public boolean hasNext()
    {
        return mCur<mValues.size();
    }

    /**
     * This method advances the iteration and returns the last value iterated through
     * @return - Returns the data in mValues based on where we are in the iteration
     */
    @Override
    public E next()
    {
        return mValues.get(mCur++);
    }




}
