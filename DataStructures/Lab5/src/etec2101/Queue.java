package etec2101;

public class Queue<E>
{
    protected LinkedList<E> mList;


    public Queue()
    {
        mList = new LinkedList<E>();
    }

    /**
     * Adds data to the queue
     * @param val- the data that is added to the end of the queue
     */
    public void push(E val)
    {
        mList.addToEnd(val);
    }

    /**
     * removes the beginning data in the list
     * @return - The data at the end of the list
     */
    public E pop()
    {
        E val = mList.getmBegin().getmValue();

        mList.remove(mList.getmBegin());
        return val;
    }

    /**
     *
     * @return - the data that is at the beginning of the list
     */
    public E peek()
    {
        E val;
        if (mList.getmBegin()==null)
        {
            val = null;
        }
        else
        {
            val = mList.getmBegin().mValue;
        }
        return val;
    }

    /**
     *
     * @return - the length of the queue
     */
    public int length()
    {
        return mList.length();

    }

    /**
     *
     * @return - the list of data in the queue
     */
    public LinkedList<E> getmList() {
        return mList;
    }

}
