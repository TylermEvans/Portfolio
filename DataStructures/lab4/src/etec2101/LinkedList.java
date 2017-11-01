package etec2101;

import java.util.Iterator;
import java.util.NoSuchElementException;


public class LinkedList <T>
{
    /**
     * This class implements the Iterator interface as is used to traverse (either forward or backwards) through
     * the attached LinkedList.  These iterators are meant to be created by calling the iterator or riterator
     * methods of the LinkedList class.
     */
    public class LinkedListIterator implements Iterator<T>
    {
        /**
         * The current node in our traversal
         */
        Node mCurNode;

        /**
         * This is the node visited previous to the current node (or null if none have been visited)
         */
        Node mLastNodeAccessed;         // used by remove.

        /**
         * A reference to the "attached" LinkedList
         */
        LinkedList<T> mList;

        /**
         * true: this is a forward iterator; false: this is a backwards iterator.
         */
        boolean mIsForward;

        /**
         * Used to ensure that we only remove once using the iterator.
         */
        boolean mCanRemove;


        /**
         * The constructor.  This is private so we can only create instances using the LinkedList iterator or
         * riterator methods.
         * @param L: The attached LinkedList
         * @param N: The starting node
         * @param is_fwd: true if this is meant to be a forward iterator, false for backwards.
         */
        private LinkedListIterator(LinkedList<T> L, Node N, boolean is_fwd)
        {
            mCurNode = N;
            mList = L;
            mIsForward = is_fwd;
            mCanRemove = false;
            mLastNodeAccessed = null;
        }

        /**
         * @return: true if there are more nodes to be returned, false if we've reached the end of the LinkedList.
         */
        @Override
        public boolean hasNext()
        {
            return mCurNode != null;
        }

        /**
         * Returns the current node and advances the internal node pointer.
         * @return
         */
        @Override
        public T next()
        {
            if (mCurNode == null)
                throw new NoSuchElementException("next called before validating with hasNext");
            
            T val = mCurNode.mValue;
            mLastNodeAccessed = mCurNode;
            if (mIsForward)
                mCurNode = mCurNode.mNext;
            else
                mCurNode = mCurNode.mPrev;
            
            mCanRemove = true;
            
            return val;
        }


        /**
         * Removes the last object returned by next.  It is an error to call this before calling next.  It is also
         * an error to call remove more than once.
         */
        @Override
        public void remove()
        {
            // Removes the last element returned by next
            if (mLastNodeAccessed == null || !mCanRemove)
            {
                // The user is meant to call next before calling this method.
                // If prev is null it likely indicates some error condition.
                throw new IllegalStateException("There is no current node to remove");
            }
                
            mList.remove(mLastNodeAccessed);
        }
        
    }


    /**
     * This Node class is meant to be used internally.  It represents one link in a LinkedList and contains
     * pointers to the previous and following node in the linked list.  It also contains a data element (of type T)
     * [sometimes called the "payload"].  By making this class protected, we ensure that outside of the LinkedList
     * class, this class isn't even visible.
     */
    protected class Node
    {
        /**
         * The data value at this position in the linked list.
         */
        T mValue;

        /**
         * The previous node in the linked list (or null if this is the first node)
         */
        Node mPrev;

        /**
         * The next node in the linked list (or null if this is the last node)
         */
        Node mNext;

        /**
         * The constructor for the node class
         * @param value: The data value to store in this node.
         */
        public Node(T value)
        {
            mValue = value;
            mPrev = mNext = null;
        }

        public T getmValue() {
            return mValue;
        }
    }

    /**
     * A reference to the beginning (head) node of the linked list.  Will be null if the list is empty.
     */
    protected Node mBegin;

    /**
     * A reference to the end (tail) node of the linked list.  Will be null if this list is empty.
     */
    public Node mEnd;

    /**
     * The number of nodes currently being stored in the linked list.
     */
    protected int mSize;

    /**
     * The LinkedList constructor.
     */
    public LinkedList()
    {
        mSize = 0;
        mBegin = mEnd = null;
    }


    /**
     * Adds a new value (and creates a node) at the end of the linked list.
     * @param value
     */
    public void addToEnd(T value)
    {
        Node new_node = new Node(value);
        if (mSize == 0)
            mBegin = mEnd = new_node;
        else
        {
            new_node.mPrev = mEnd;
            mEnd.mNext = new_node;
            mEnd = new_node;
        }
        mSize++;
    }


    /**
     * Adds a new value (and creates a node) at the beginning of the linked list.
     * @param value
     */
    public void addToBegin(T value)
    {
        Node new_node = new Node(value);
        if (mSize == 0)
            mBegin = mEnd = new_node;
        else
        {
            new_node.mNext = mBegin;
            mBegin.mPrev = new_node;
            mBegin = new_node;
        }
        mSize++;
    }

    /**
     * @return: The length of the list.
     */
    public int length()
    {
        return mSize;
    }


    /**
     * @return: A formatted string representation of the contents of this linked list
     */
    @Override
    public String toString()
    {
        String s = "<";
        Node n = mBegin;
        if (n == null)
            s += "empty";
        else
        {
            while (n != null)
            {
                s += "[" + n.mValue.toString() + "]";
                n = n.mNext;
            }
        }
        return s + ">";
    }


    /**
     * The indexing-like operator for our linked list.  Note how this is an O(n) operation.  For arrays, this
     * operation would be O(1)
     * @param position: The position.  Must be in the range 0...size-1
     * @param is_fwd: true if we're measuring from the front, false if we're measuring from the back
     * @return: The value at that position.
     * @throws IndexOutOfBoundsException
     */
    public T at(int position, boolean is_fwd) throws IndexOutOfBoundsException
    {
        LinkedListIterator LI;
        if (is_fwd)
            LI = iterator();
        else
            LI = riterator();

        int curPos = 0;
        T result;
        while (LI.hasNext())
        {
            if (curPos == position)
                return LI.next();
            else
            {
                curPos++;
                LI.next();      // Just discard the result.
            }
        }

        // If we get here, we walked off the end of the list before finding the requested position.
        throw new IndexOutOfBoundsException();
    }


    /**
     * Similar to the other version of at, but assumes we want a forward-index.
     * @param position: position in the list
     * @return: The value at that position
     * @throws IndexOutOfBoundsException
     */
    public T at(int position) throws IndexOutOfBoundsException
    {
        return at(position, true);
    }


    /**
     * Inserts a new node at the given position in the linked List, "shoving" every other node after forward
     * @param position
     * @param value
     */
    public void insert(int position, T value) throws IndexOutOfBoundsException
    {
        Node newNode = new Node(value);

        if (position == 0)
        {
            addToBegin(value);
            return;
        }
        else if (position == mSize)
        {
            addToEnd(value);
            return;
        }
        else
        {
            // The more challenging case -- we're somewhere in the middle.
            Node N = mBegin;
            int curPos = 0;
            while (curPos != position && N != null)
            {
                N = N.mNext;
                curPos++;
            }

            if (N == null)
                throw new IndexOutOfBoundsException("Invalid position (" + position + ")");
            else
            {
                newNode.mNext = N;
                newNode.mPrev = N.mPrev;

                N.mPrev.mNext = newNode;
                N.mPrev = newNode;
            }
        }

        // We now have one more node.
        mSize++;
    }


    /**
     * @return: A forward-advancing iterator
     */
    public LinkedListIterator iterator()
    {
        LinkedListIterator I = new LinkedListIterator(this, mBegin, true);
        return I;
    }

    /**
     * @return: A backwards-advancing iterator
     */
    public LinkedListIterator riterator()
    {
        LinkedListIterator I = new LinkedListIterator(this, mEnd, false);
        return I;
    }


    /**
     * This is meant to be an internal-only helper method (hence the private
     * access modifier).  It is used by removeAll and the LinkedListIterator.remove
     * method.
     * @param n
     */
    public void remove(Node n)
    {
        if (n == mBegin && n == mEnd)
        {
            // One element list -- destroy it!
            mBegin = mEnd = null;
        }
        else if (n == mBegin)
        {
            // We're removing the first element in an at-least 2 element list
            mBegin = n.mNext;
            mBegin.mPrev = null;
        }
        else if (n == mEnd)
        {
            // We're removing the end element in an at-least 2 element list.
            mEnd = n.mPrev;
            mEnd.mNext = null;
        }
        else
        {
            // We're removing the middle element
            n.mNext.mPrev = n.mPrev;
            n.mPrev.mNext = n.mNext;
        }

        // Decrement the size to account for the removed node.
        mSize--;
    }


    /**
     * Removes all occurrences of val and returns the number of occurrences removed.
     * @param val: The value to remove
     * @return: the number of occurrences removed
     */
    public int removeAll(T val)
    {
        int count = 0;
        Node n = mBegin;
        while (n != null)
        {
            if (n.mValue.equals(val))
            {
                count++;
                
                remove(n);
            }
            
            n = n.mNext;
        }
        
        return count;
    }


    /**
     * @param val: The value of interest
     * @return: The number of occurrences of that value
     */
    public int count(T val)
    {
        int total = 0;
        Node n = mBegin;
        while (n != null)
        {
            if (n.mValue.equals(val))
                total++;
            n = n.mNext;
        }
        return total;
    }

    public Node getmEnd() {
        return mEnd;
    }

    public Node getmBegin() {
        return mBegin;
    }

}
