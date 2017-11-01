package etec2101;
public class Stack<E>
{
    protected LinkedList<E> mList;

    public Stack()
    {
        mList = new LinkedList<E>();
    }

    /**
     * adds a data value to the end of the stack
     * @param val any type a data
     */
    public void push(E val)
    {
        mList.addToEnd(val);
    }

    /**
     * removes the data item at the end of the list
     */
    public void pop()
    {
        mList.remove(mList.mEnd);
    }

    /**
     * Sets the val to null if the end of the stack is empty
     * @return - the data type at the end of the stack
     */
    public E peek()
    {
        E val;
        if (mList.mEnd==null)
        {
            val = null;
        }
        else
        {
            val = mList.mEnd.mValue;
        }
        return val;

    }

    /**
     *
     * @return - the list of data in the stack
     */
    public LinkedList<E> getmList() {
        return mList;
    }
}
