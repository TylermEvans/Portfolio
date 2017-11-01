package etec2101;


public class HashMap<K,V>
{
    int mCap;
    int mCapIncrease;
    float mLoadCap;
    float mSize;
    float maxLoad;
    Object[] mTable;
    protected class Node
    {
        K mKey;
        V mValue;
        public Node(K k, V v)
        {
            mKey = k;
            mValue = v;
        }

        public V getmValue() {
            return mValue;
        }
    }
    public HashMap(int init, float max, int increase)
    {
        mSize = 0;
        mCap = init;
        mCapIncrease = increase;
        maxLoad = max;
        mTable = new Object[mCap];
    }

    public void set(K key, V value)
    {
        //mLoadCap = (mSize/mCap);
        //if (mLoadCap>=maxLoad)
        //{
           // Object[] temp = mTable;
            //mTable = new Object[mCap+mCapIncrease];
            //for (int i=0; i<temp.length; i++)
            //{
             //   Object t=temp[i];
             //   Node n = (Node)t;
             //   if (t!=null)
             //   {
               //     this.set(n.mKey,n.mValue);
                //    mSize++;

              //  }
            //}
       // }

        Node n = new Node(key,value);
        int index = HashTo(n.mKey);
        mTable[index] = n;



    }
    public V get(K key)
    {
        int index = HashTo(key);
        Node n = (Node)mTable[index];
        return n.getmValue();
    }

    public int HashTo(K key)
    {
        int k = key.hashCode();
        int index = k%mCap;

        Node n = (Node)mTable[index];
        if (mTable[index]==null || n.mKey==key)
        {
            return index;

        }
        else
        {
            while(mTable[index]!=null && n.mKey!=key)
            {
                index++;
            }

        }
        if (index>mTable.length)
        {
            index = 0;

        }
        return index;

    }

    public int getHeight()
    {
        return (int)mSize;
    }

    public void remove(K key)
    {

        int index = HashTo(key);
        mTable[index] = null;

    }

    public HashMapIterator iterator()
    {
       HashMapIterator i = new HashMapIterator();
        return i;
    }
    public enum TraversalType
    {


    }

    public Object[] getmTable() {
        return mTable;
    }

    @Override
    public String toString()
    {
        String result =  "{ ";
        for (int i = 0; i<mTable.length; i++)
        {
            String stuff;
            if (mTable[i]!=null)
            {

                Node t =(Node)mTable[i];
                stuff = t.mKey+":"+t.mValue+" , ";


                result+=stuff;


            }


        }
        result+=" }";


        return result;
    }
}

