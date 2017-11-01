import java.util.*;

/**
 * This is my BinaryHeap class. This class creates a BinaryHeap, It can either be a MinHeap or
 * a MaxHeap. The heaps are arrays internally.
 * @param <N> - An Abstract Java variable. Extends from Comparable so that it may be compared to
 *           other objects of the same "type"
 */
public class BinaryHeap<N extends Comparable>
{
    protected MinHeap mMinheap; //An empty Minheap Object
    protected MaxHeap mMaxheap; // An empty Maxheap Object
    protected HeapType mType; // The type of heap desired

    /**
     * The first constructor takes one parameter, a HeapType enum that specifies what kind of heap we want.
     * @param type - An enum that tells the Binaryheap what kind of heap is desired
     */
    public BinaryHeap(HeapType type)
    {
        mType = type;
        if (type==HeapType.MAXHEAP)
        {
            mMaxheap = new MaxHeap();
        }
        else
        {
            mMinheap = new MinHeap();

        }
    }

    /**
     * This is the second constructor, also asks for a Java collection. This parameter is passed on to the Minheap or Maxheap
     * depending on what Heaptype is passed
     * @param type
     * @param c
     */
    public BinaryHeap(HeapType type, Collection c )
    {
        mType = type;
        if (type==HeapType.MAXHEAP)
        {
            mMaxheap = new MaxHeap(c);
        }
        else
        {
            mMinheap = new MinHeap(c);

        }

    }


    /**
     * An enum called HeapType. Used to decide what heap is needed
     */
    public enum HeapType
    {
        MAXHEAP,MINHEAP


    }

    /**
     *This is the MinHeap class. This class by the least valued object in the array
     * @param <N> - A java generic. Extends Comparable so that it may be compared to other generics of its "type"
     */
    public class MinHeap<N extends Comparable>
    {
        protected ArrayList mArray;//The ArrayList
        protected  int mSize; //The Number of objects in the Array

        /**
         * This is the first constructor. It just initializes the Array and adds null to the first entry
         */
        public MinHeap()
        {
            mArray = new ArrayList();
            mArray.add(null);
            mSize = 0;

        }

        /**
         * This is the second Constructor. Takes a Java collection parameter and iterates through it
         * Pushes all of the collections data into the heap
         * @param c - The java Collection
         */
        public MinHeap(Collection c)
        {
            mArray = new ArrayList();
            mArray.add(null);
            mSize = 0;
            Iterator I = c.iterator();
            while (I.hasNext())
            {
                N cur = (N)I.next();
                this.push(cur);
            }

        }

        /**
         * This is the Push Method for the MinHeap. This method pushes the data into the heap while
         * also preforming the bubble up procedure
         * @param data - A java generic data type
         */
        public void push(N data)
        {

            int index = mArray.size();
            mArray.add(index,data);
            int parentindex = index >> 1;
            if (parentindex!=0)// This checks to if we are the first parent in the list(The actual first parent is index 0 or null, without this the program crashes)
            {
                while (index >= 1 &&  ((N)mArray.get(index)).compareTo((N)mArray.get(parentindex))<0) // if the child is less than the parent then they switch.
                {
                    N parent = (N)mArray.get(parentindex);
                    N child = (N)mArray.get(index);
                    mArray.set(index,parent);
                    mArray.set(parentindex,child);
                    index = parentindex;
                    parentindex = index >> 1;
                    if (parentindex<1)
                    {
                        break;

                    }

                }

            }
            mSize++;
        }

        /**
         * This is a getter method that gets the size of the MinHeap
         * @return - an integer that tells us the size
         */
        public int size()
        {
            return mSize;

        }

        /**
         * This is the pop method for the MinHeap. It also preforms the percolating down procedure
         * @return - returns the data at index 1(or the root of the heap)
         */
        public N pop() {
            N root = (N)mArray.get(1);
            N end = (N)mArray.get(mArray.size()-1);
            mArray.set(1,end);
            mArray.set(mArray.size()-1,root);
            mArray.remove(mArray.size()-1);//Removes the newly switched data that is now at the end of the heap
            int index = 1;
            int best = bestChild(index);
            while (best > 0 && outOfOrder(index,best))//percolates down
            {

                N parent = (N)mArray.get(index);
                N child = (N)mArray.get(best);
                mArray.set(index,child);
                mArray.set(best,parent);
                index = best;
                best = bestChild(index);

            }
            mSize--;
            return root;
        }

        /**
         * This is a helper method for the pop. This method gives the correct child depending on if we have 0 children, 1 or 2 children
         * @param index - The start index
         * @return - An integer representing the index of the child. Also used to determine if we have more children
         */
        public int bestChild(int index)
        {
            int result;
            int leftchildindex = index << 1;
            int rightchildindex = leftchildindex + 1;

            if(leftchildindex>=mArray.size())
            {
                result = -1;
            }
            else if(rightchildindex>=mArray.size())
            {
                result = leftchildindex;

            }
            else
            {
                if (mType==HeapType.MAXHEAP)
                {
                    result = largestIndex(leftchildindex,rightchildindex);
                }
                else
                {
                    result = smallestIndex(leftchildindex,rightchildindex);
                }
            }
            return result;
        }

        /**
         * This is a helper method for the pop. This method compares the parents to their best child. if they are outoforder(This depends on the HeapType)
         * it returns true
         * @param index - The parents index
         * @param best - The bestchilds index
         * @return - A boolean indicating whether we are out of order
         */
        public boolean outOfOrder(int index, int best)
        {
            boolean result;
            if (mType==HeapType.MAXHEAP)
            {
                N parent = (N)mArray.get(index);
                N bestchild = (N)mArray.get(best);
                if (parent.compareTo(bestchild)<0)
                {
                    result = true;
                }
                else
                {
                    result = false;
                }
            }
            else
            {
                N parent = (N)mArray.get(index);
                N bestchild = (N)mArray.get(best);
                if (parent.compareTo(bestchild)>0)
                {
                    result = true;
                }
                else {
                    result = false;
                }
            }
            return result;
        }

        /**
         * This is a helper method used in the bestChild. Determines which child is bigger
         * @param leftindex - the leftchild index number
         * @param rightindex - the rightchild index number
         * @return - The index that corresponds to the child with the largest data
         */
        public int largestIndex(int leftindex,int rightindex)
        {
            int result;
            N leftchild = (N)mArray.get(leftindex);
            N rightchild = (N)mArray.get(rightindex);

            if (leftchild.compareTo(rightchild)>0)
            {
                result = leftindex;

            }
            else
            {
                result = rightindex;

            }
            return result;


        }

        /**
         * This is a helper method used in the bestChild method. Determines which child is smaller
         * @param leftindex - The leftchild index
         * @param rightindex - The rightchild index
         * @return - The index that corresponds to the child with the smallest data
         */
        public int smallestIndex(int leftindex, int rightindex)
        {
            int result;
            N leftchild = (N)mArray.get(leftindex);
            N rightchild = (N)mArray.get(rightindex);
            if (leftchild.compareTo(rightchild)<0)
            {
                result = leftindex;
            }
            else
            {
                result = rightindex;
            }
            return result;
        }






    }


    /**
     *This the MaxHeap class. Does the same stuff as the MinHeap, except it sorts by greatest values instead of smallest
     * @param <N> - A java Generic
     */
    public class MaxHeap<N extends Comparable>
    {
        protected ArrayList mArray;
        protected int mSize;

        /**
         * Initializes the Heap
         */
        public MaxHeap()
        {
            mArray = new ArrayList();
            mArray.add(null);
            mSize = 0;

        }

        /**
         * initializes the heap and adds the values from a java collection to the heap
         * @param c - A java collection
         */
        public MaxHeap(Collection c)
        {
            mArray = new ArrayList();
            mArray.add(null);
            mSize = 0;
            Iterator I = c.iterator();
            while (I.hasNext())
            {
                N cur = (N)I.next();
                mArray.add(cur);
            }

        }

        /**
         * This is the Push Method for the MaxHeap. This method pushes the data into the heap while
         * also preforming the bubble up procedure
         * @param data - A java generic data type
         */
        public void push(N data)
        {

            int index = mArray.size();
            mArray.add(index,data);
            int parentindex = index >> 1;
            if (parentindex!=0)
            {
                while (index >= 1 &&  ((N)mArray.get(index)).compareTo((N)mArray.get(parentindex))>0)// if the child is greater than the parent bubble up
                {
                    N parent = (N)mArray.get(parentindex);
                    N child = (N)mArray.get(index);
                    mArray.set(index,parent);
                    mArray.set(parentindex,child);
                    index = parentindex;
                    parentindex = index >> 1;
                    if (parentindex<1)
                    {
                        break;

                    }

                }

            }
            mSize++;

        }
        /**
         * This is a getter method that gets the size of the MaxHeap
         * @return - an integer that tells us the size
         */
        public int size()
        {
            return mSize;

        }
        /**
         * This is the pop method for the MinHeap. It also preforms the percolating down procedure
         * @return - returns the data at index 1(or the root of the heap)
         */
        public N pop()
        {
            N root = (N)mArray.get(1);
            N end = (N)mArray.get(mArray.size()-1);
            mArray.set(1,end);
            mArray.set(mArray.size()-1,root);
            mArray.remove(mArray.size()-1);
            int index = 1;
            int best = bestChild(index);
            while (best > 0 && outOfOrder(index,best))
            {

                N parent = (N)mArray.get(index);
                N child = (N)mArray.get(best);
                mArray.set(index,child);
                mArray.set(best,parent);
                index = best;
                best = bestChild(index);

            }
            mSize--;
            return root;

        }


        /**
         * This is a helper method for the pop. This method gives the correct child depending on if we have 0 children, 1 or 2 children
         * @param index - The start index
         * @return - An integer representing the index of the child. Also used to determine if we have more children
         */
        public int bestChild(int index)
        {
            int result;
            int leftchildindex = index << 1;
            int rightchildindex = leftchildindex + 1;

            if(leftchildindex>=mArray.size())
            {
                result = -1;
            }
            else if(rightchildindex>=mArray.size())
            {
                result = leftchildindex;

            }
            else
            {
                if (mType==HeapType.MAXHEAP)
                {
                    result = largestIndex(leftchildindex,rightchildindex);
                }
                else
                {
                    result = smallestIndex(leftchildindex,rightchildindex);
                }
            }
            return result;
        }

        /**
         * This is a helper method for the pop. This method compares the parents to their best child. if they are outoforder(This depends on the HeapType)
         * it returns true
         * @param index - The parents index
         * @param best - The bestchilds index
         * @return - A boolean indicating whether we are out of order
         */
        public boolean outOfOrder(int index, int best)
        {
            boolean result;
            if (mType==HeapType.MAXHEAP)
            {
                N parent = (N)mArray.get(index);
                N bestchild = (N)mArray.get(best);
                if (parent.compareTo(bestchild)<0)
                {
                    result = true;
                }
                else
                {
                    result = false;
                }
            }
            else
            {
                N parent = (N)mArray.get(index);
                N bestchild = (N)mArray.get(best);
                if (parent.compareTo(bestchild)>0)
                {
                    result = true;
                }
                else {
                    result = false;
                }
            }
            return result;
        }

        /**
         * This is a helper method used in the bestChild. Determines which child is bigger
         * @param leftindex - the leftchild index number
         * @param rightindex - the rightchild index number
         * @return - The index that corresponds to the child with the largest data
         */
        public int largestIndex(int leftindex,int rightindex)
        {
            int result;
            N leftchild = (N)mArray.get(leftindex);
            N rightchild = (N)mArray.get(rightindex);

            if (leftchild.compareTo(rightchild)>0)
            {
                result = leftindex;

            }
            else
            {
                result = rightindex;

            }
            return result;


        }

        /**
         * This is a helper method used in the bestChild method. Determines which child is smaller
         * @param leftindex - The leftchild index
         * @param rightindex - The rightchild index
         * @return - The index that corresponds to the child with the smallest data
         */
        public int smallestIndex(int leftindex, int rightindex)
        {
            int result;
            N leftchild = (N)mArray.get(leftindex);
            N rightchild = (N)mArray.get(rightindex);
            if (leftchild.compareTo(rightchild)<0)
            {
                result = leftindex;
            }
            else
            {
                result = rightindex;
            }
            return result;
        }

    }

    /**
     * This is the Push method for the BinaryHeap class. This is a wrapper method that calls the correspondign MinHeap/MaxHeaps push methods.
     * @param data - The data to be added, a java generic
     */
    public void push(N data)
    {
        if (mType==HeapType.MAXHEAP)
        {
            mMaxheap.push(data);


        }
        else
        {
            mMinheap.push(data);

        }


    }

    /**
     * This is a getter method that gets the internal array from the Min or Max heap. Used to see the values in the heap
     * @return - The internal heap array/heap values
     */
    public ArrayList getHeap()
    {
        if (mType==HeapType.MAXHEAP)
        {
            return mMaxheap.mArray;
        }
        else
        {
            return mMinheap.mArray;

        }
    }

    /**
     * A wrapper method that calls the size methods of the Min/Max heap
     * @return - The size of the heap
     */
    public int size()
    {
        if (mType == HeapType.MAXHEAP)
        {
            return mMaxheap.size();

        }
        else
        {
            return mMinheap.size();

        }
    }

    /**
     * A wrapper method that calls the pop methods of the Min/Max heap
     * @return - The root data of the heap.
     */
    public N pop()
    {
        N result;
        if (mType==HeapType.MAXHEAP)
        {
            result = (N)mMaxheap.pop();
        }
        else
        {
            result = (N)mMinheap.pop();
        }
        return result;

    }












}
