package etec2101;
import java.util.*;
public class LinkedList<E>
{
    protected Node mBegin;
    protected Node mEnd;
    protected int mSize;



    public LinkedList()
    {
        mBegin = null;
        mEnd = null;
        mSize = 0;

    }

    protected class Node
    {
        protected  Node mNext;
        protected  Node mPrev;
        protected  E mValue;


        public Node(E val)
        {
            mValue = val;
            mNext = null;
            mPrev = null;

        }

        public E getmValue() {
            return mValue;
        }
    }
    public class LinkedListIterator implements Iterator<E>
    {
        private Node current;
        private boolean dir;


        private LinkedListIterator(boolean t)
        {
            dir = t;
            if (dir == true){
                current = mBegin;
            }
            else
            {
                current = mEnd;

            }



        }

        public boolean hasNext()
        {
            boolean result;
            result = current!=null;
            return result;
        }


        public E next()
        {
            E result;
            result = current.mValue;
            if (hasNext())
            {
                if (dir)
                {
                    current = current.mNext;
                }
                else
                {
                    current = current.mPrev;
                }
            }
            return result;
        }

        public void remove()
        {

            if (mSize==1)
            {
                mBegin = null;
                mEnd = null;

            }
            if (dir)
            {
                if(current.mPrev.mPrev==null) //checks if the previous is the head
                {
                    current.mPrev.mNext = null;
                    current.mPrev = null;
                    mBegin = current;

                }
                else
                {
                    current.mPrev = current.mPrev.mPrev;
                    current.mPrev.mNext = current;

                }
            }
            else
            {
                if(current.mNext.mNext==null)
                {
                    current.mNext.mPrev = null;
                    current.mNext = null;
                    mEnd = current;
                }
                else
                {
                    current.mNext = current.mNext.mNext;
                    current.mNext.mNext.mPrev = current;

                }
            }

        }
        public void addAfter(E val)
        {
            if (current.mNext==null)
            {
                addToEnd(val);
            }
            else
            {
                Node newN = new Node(val);
                newN.mPrev = current;
                newN.mNext = current.mNext;
                newN.mNext.mPrev = newN;
                newN.mPrev.mNext = newN;
            }



        }
        public void addBefore(E val)
        {
            dir = !dir;
            addAfter(val);
            dir = !dir;
        }









    }
    public LinkedListIterator iterator()
    {
        return new LinkedListIterator(true);


    }

    public LinkedListIterator riterator()
    {
        return new LinkedListIterator(false);


    }

    public void addToEnd(E val)
    {
        Node n = new Node(val);
        if (mSize==0)
        {
            mBegin = mEnd = n;
        }
        else
        {
            mEnd.mNext = n;
            n.mPrev = mEnd;
            mEnd = n;

        }
        mSize++;

    }
    public void addToBegin(E val)
    {
        Node n = new Node(val);
        if (mSize==0)
        {
            mBegin = mEnd = n;

        }
        else
        {
            mBegin.mPrev = n;
            n.mNext = mBegin;
            mBegin = n;

        }
        mSize++;

    }

    public int length()
    {
        return mSize;
    }


    @Override
    public String toString()
    {   String s = "<";
        if (mSize==0)
        {
            s+="empty";
        }
        else
        {
            for (int i = 0; i<mSize; i++)
            {
                s+="[";
                s+=at(i);
                s+="]";

            }
            s+=">";

        }
        return s;
    }
    public int count(E val)
    {
        int result = 0;
        for (int i=0; i<mSize; i++)
        {
            if (val.equals(at(i)))
            {
                result++;
            }
        }
        return result;
    }
    public E at(int pos, boolean start)
    {
        LinkedListIterator i;
        if(pos>mSize || pos<=0)
        {


        }
        if (start)
        {
            i = iterator();

        }
        else
        {
            i = riterator();

        }
        for (int t=0; t<pos; t++)
        {
            i.next();

        }
        return i.current.mValue;





    }
    public E at (int pos)
    {
        return at(pos,true);

    }
    public void insert(int pos, E data)
    {
        if (pos>mSize || pos<0)
        {
            throw new IndexOutOfBoundsException("bad stuff");

        }

        LinkedListIterator i = iterator();
        if (pos == 0)
        {
            addToBegin(data);

        }
        else if (pos==mSize)
        {
            addToEnd(data);
        }
        else
        {

            for (int t = 0; t<pos; t++)
            {
                i.next();
            }

            i.addBefore(data);
            mSize++;

        }



    }
    public int removeAll(E val)
    {
        int result = 0;
        LinkedListIterator i = iterator();
        for (int t = 0; t<mSize-1; t++)
        {
            i.next();

        }
        if (i.current.mValue==val)
        {
            result++;
            i.remove();

        }

        return result;
    }






}
