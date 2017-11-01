package etec2101;


import java.util.ArrayList;

/**
 * Creates a Node that is used in a Binary Search Tree. Extends from the Comparable class.
 * These nodes are never made inbdividually, they are made through the BinarySearchTree class
 * mData - The payload or data held within the node
 * mLeft - The left node reference, The lefts data is than the value of this nodes data
 * mRight - The right node reference, the rights data is greater than the value of this nodes data
 * @param <E> Generic Parameter. Allows for the BstNode to hold any type of data.
 */
class BSTnode<E extends Comparable> {
    //Variables
    protected E mData;
    protected BSTnode mLeft;
    protected BSTnode mRight;

    /**
     * This is the BSTnode constructor. Sets the mData attribute to the value passed, sets the references to null initially.
     * @param val - Takes a generic data type for the payload
     */
    public BSTnode(E val) {
        mData = val;
        mLeft = mRight = null;
    }

    /**
     * This method adds a node to the BinarySearchTree. If the passed value is greater than or equal to mData, mRight is set to reference a new node
     * with the passed value. If the value is less than mData, than mLeft is set to reference a new node with the lesser value
     * @param val Takes a generic data value
     */
    public void add(E val) {
        if (mData.compareTo(val) > 0) {
            if (mLeft == null) {
                mLeft = new BSTnode(val);
            } else {
                mLeft.add(val);
            }
        } else {
            if (mRight == null) {
                mRight = new BSTnode(val);
            } else {
                mRight.add(val);
            }
        }
    }

    /**
     * Goes down the Left and Right paths of the tree until it reaches null. Recursively calls getHeight on each node in the tree to get the total Tree height
     * @return - Returns the sums of the left and right heights of the tree
     */
    public int getHeight() {
        int L = 0;
        int R = 0;
        if (mLeft != null) {
            L = mLeft.getHeight();
        }
        if (mRight != null) {
            R = mRight.getHeight();
        }
        return L > R ? L + 1 : R + 1;
    }

    /**
     *This method takes a data value. This data value is compared to the other values in this tree recursively. The total amount
     * of times this val is in the tree is the value that is returned.
     * @param val - A generic data type
     * @return - Returns an integer type.
     */
    public int count(E val) {
        if (mData.compareTo(val) == 0) {
            if (mRight == null) {
                return 1;
            } else {
                return mRight.count(val) + 1;
            }
        } else if (mData.compareTo(val) < 0) {
            if (mRight == null) {
                return 0;


            } else {
                return mRight.count(val);

            }
        } else {
            if (mLeft == null) {
                return 0;

            } else {
                return mLeft.count(val);

            }


        }
    }

    /**
     * This method Recursively adds the data to a string that is tabbed over based on the depth value of the tree
     * @param depth - The depth of the tree, represents how many tab overs we need
     * @return - Returns a String representation of the tree
     */
    protected String toStringHelper(int depth) {
        String temp = "";



        for (int i = 0; i < depth; i++) {

            temp += "\t";


        }
        temp+="[";

        temp += mData +"]" + "\n";



        if (mLeft != null) {
            temp += mLeft.toStringHelper(depth + 1);

        }

        if (mRight != null) {
            temp += mRight.toStringHelper(depth + 1);
        }


        return temp;

    }

    /**
     * This method builds an ArrayList for use in the BSTiterator class. This ArrayList is either a Pre-order traversal, Post-order, or In-order Traversal.
     * The end product is an ArrayList that has all of the values in it based on one of these traversals. This methods uses Recursion to build the array.
     * @param a - an ArrayList that is within the BSTIterator class. Initially empty.
     * @param t - The Traversal Type that detrermines how the arrayList is built.
     */
    public void buildArrayList(ArrayList a, BinarySearchTree.TraversalType t)
    {
        if (BinarySearchTree.TraversalType.In==t)
        {

            if(mLeft!=null)
            {
                mLeft.buildArrayList(a,t);
            }
            a.add(mData);
            if(mRight!=null)
            {
                mRight.buildArrayList(a,t);

            }
        }
        else if (BinarySearchTree.TraversalType.Pre==t)
        {
            a.add(mData);
            if (mLeft!=null)
                mLeft.buildArrayList(a,t);
            if (mRight!=null)
                mRight.buildArrayList(a,t);
        }
        else
        {
            if(mLeft!=null)
                mLeft.buildArrayList(a,t);
            if (mRight!=null)
                mRight.buildArrayList(a,t);
            a.add(mData);

        }

    }
}

